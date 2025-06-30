from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int

    model_config = {
        "from_attributes": True  # ✅ Required in Pydantic v2
    }

class ReviewBase(BaseModel):
    content: str

class ReviewCreate(ReviewBase):
    book_id: int

class ReviewOut(ReviewBase):
    id: int
    book_id: int

    model_config = {
        "from_attributes": True  # ✅ Required in Pydantic v2
    }

