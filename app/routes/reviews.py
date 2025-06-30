from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud, deps

router = APIRouter()

@router.post("/reviews", response_model=schemas.ReviewOut, status_code=201)
def add_review(review: schemas.ReviewCreate, db: Session = Depends(deps.get_db)):
    return crud.create_review(db, review)

@router.get("/reviews", response_model=list[schemas.ReviewOut])
def get_reviews(db: Session = Depends(deps.get_db)):
    return crud.get_reviews(db)
