class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # Base book format
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call parent constructor
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        # EBook specific format
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call parent constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        # PrintBook specific format
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []  # composition: Library HAS books

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            # __str__ from each class is used
            print(book)
