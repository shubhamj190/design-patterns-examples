"""This is an example and explanation of pydantic"""

import json

from typing import Optional, List
from pydantic import BaseModel, validator, root_validator


class ISNBMissinException(Exception):
    def __init__(self, title, message) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class ISBN10FormatError(Exception):
    def __init__(self, value, message) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Book(BaseModel):
    title: str
    subtitle: Optional[str]
    author: str
    publisher: str
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    price: float

    @validator("isbn_10")
    @classmethod
    def isbn_10_validator(cls, value):
        """validation to check if isbn value is valid or not"""

        char = [c for c in value if c in "0123456789Xx"]

        if len(char) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        if sum((10 - i) * char_to_int(x) for i, x in enumerate(char)) % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11."
            )
        return value

    @root_validator(pre=True)
    @classmethod
    def check_isbn10_isbn13(cls, value):
        if "isbn_10" not in value and "isbn_13" not in value:
            raise ISNBMissinException(
                title=value["title"],
                message="Document should have either an ISBN10 or ISBN13",
            )
        return value

    class Config:
        allow_mutation: False
        anystr_lower = True


with open("data.json") as file:
    data = json.load(file)
    books: List[Book] = [Book(**item) for item in data]
    print(books[0])
