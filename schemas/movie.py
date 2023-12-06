from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=1, max_length=200)
    overview: str = Field(min_length= 3, max_length=400)
    year: int = Field(le=2023)
    rating: str = Field(min_length=0, max_length=30)
    category: str = Field(min_length=1, max_length=100)

