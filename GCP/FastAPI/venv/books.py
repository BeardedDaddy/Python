"""
From the fasttapi module import FastAPI
"""

from fastapi import FastAPI

""" 
From the pydantic module import BaseModel and Field 
"""

from pydantic import BaseModel, Field

""" 
From the uuid module import the UUID
"""

from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)
    
BOOKS = ["The You You Know", "Stop Saying Yes When You Mean No", "Just Because You Can Doesn't Mean You Should"]  # noqa


@app.get('/{name}')
def read_api(name: str):
    return {'Welcome': name}

@app.post("")
def create_book(book: Book):
    BOOKS.append(book)
    return book