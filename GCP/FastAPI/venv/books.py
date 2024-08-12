"""From the uuid module import the UUID"""

from uuid import UUID

"""From the fasttapi module import FastAPI and HTTPExceptions"""

from fastapi import FastAPI, HTTPException

"""From the pydantic module import BaseModel and Field"""

from pydantic import BaseModel, Field

app = FastAPI()


class Book(BaseModel):
    """Creating a class called BaseModel to validate the data"""
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)


BOOKS = ["The You You Know",
         "Stop Saying Yes When You Mean No",
         "Just Because You Can Doesn't Mean You Should"]


@app.get('/')
def read_api():
    """This class reads an empty parameter and returns the list of books"""
    return BOOKS


@app.post("/")
def create_book(book: Book):
    """Created a class called create_book with a boo  and a"""
    BOOKS.append("book")
    return book


@app.put("/{book_id}")
def update_book(book_id: UUID, book: Book):
    """This class, called update_book, the book object as a parameter"""
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]

    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} : Does not exist"
    )


@app.delete("/{book_id}")
def delete_book(book_id: UUID):
    """This delete_book function will delete books with the same UUID book_id"""  # noqa
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f"ID: {book_id} deleted"
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} : Does not exist"
    )
