# book_class.py

class Book:
    def __init__(self, title, author, year):
        # Constructor to initialize attributes
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Destructor to print deletion message
        print(f"Deleting {self.title}")

    def __str__(self):
        # String representation of the book for print
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official string representation (to recreate the Book instance)
        return f"Book('{self.title}', '{self.author}', {self.year})"
