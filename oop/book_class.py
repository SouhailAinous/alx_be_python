# alx_be_python/oop/book_class.py

class Book:
    """A simple Book class demonstrating magic methods."""

    def __init__(self, title: str, author: str, year: int):
        # Constructor (__init__): Initializes a Book instance with title, author, and year.
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Destructor (__del__): Prints "Deleting (title of the book)" upon object deletion.
        # Expected exact output example: "Deleting 1984"
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        # String Representation (__str__):
        # Returns: "(title) by (author), published in (year)"
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        # Official Representation (__repr__):
        # Returns that would recreate the Book instance exactly:
        # f"Book('{self.title}', '{self.author}', {self.year})"
        return f"Book('{self.title}', '{self.author}', {self.year})"
