# library_system.py

# Base class for Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Derived class EBook inheriting from Book
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size  # Specific attribute for EBook

# Derived class PrintBook inheriting from Book
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count  # Specific attribute for PrintBook

# Library class that uses composition to manage books
class Library:
    def __init__(self):
        self.books = []  # List to hold books

    def add_book(self, book):
        # Adds a book to the library
        self.books.append(book)

    def list_books(self):
        # Prints details of all books in the library
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
