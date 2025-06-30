from sqlalchemy.orm import Session
from . import models, schemas

# app/crud.py

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())  # ✅ replace .model_dump() with .dict()
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session):
    return db.query(models.Book).all()

def create_review(db: Session, review: schemas.ReviewCreate):
    db_review = models.Review(**review.dict())

    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews(db: Session):
    return db.query(models.Review).all()
