from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError

from .routes import books, reviews
from .database import Base, engine
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Review Service")

@app.exception_handler(SQLAlchemyError)
async def db_exception_handler(request: Request, exc: SQLAlchemyError):
    return JSONResponse(
        status_code=500,
        content={"message": "A database error occurred."},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Invalid data", "errors": exc.errors()},
    )

app.include_router(books.router)
app.include_router(reviews.router)
