from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud, deps, cache

router = APIRouter()

@router.get("/books", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(deps.get_db)):
    cached_books = cache.get_books_from_cache()
    if cached_books:
        return cached_books

    books = crud.get_books(db)
    result = [schemas.BookOut.from_orm(book) for book in books]

    cache.set_books_to_cache([book.dict() for book in result])
    return result


@router.post("/books", response_model=schemas.BookOut, status_code=201)
def add_book(book: schemas.BookCreate, db: Session = Depends(deps.get_db)):
    db_book = crud.create_book(db, book)
    return schemas.BookOut.from_orm(db_book)

