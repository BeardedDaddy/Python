from fastapi import FastAPI, HTTPException

"""
From the fasttapi module import FastAPI and HTTPExceptions
"""

from pydantic import BaseModel, Field

""" 
From the pydantic module import BaseModel and Field 
"""

from uuid import UUID

""" 
From the uuid module import the UUID
"""

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)


BOOKS = ["The You You Know", "Stop Saying Yes When You Mean No", "Just Because You Can Doesn't Mean You Should"]  # noqa


@app.get('/')


def read_api():
    return BOOKS

"""
This class reads an empty parameter and returns the list of books
"""

@app.post("/")
def create_book(book: Book):
    BOOKS.append(book)
    return book

"""
The above class is called create_book and has a parameter book and parses the list of books
"""

@app.put("/{book_id}")
def update_book(book_id: UUID, book: BOOK):
    counter = 0
    

for x in BOOKS:
    counter += 1
    if x.id == book_id:
        BOOKS[counter - 1] = book
        return BOOKS[counter - 1]
raise HTTPException(
    status_code= 404,
    detail= f"ID {book_id} : Does not exist"
)

def delete_book(book_id: UUID):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]