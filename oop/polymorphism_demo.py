# oop/book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor to initialize the Book instance.
        :param title: Title of the book
        :param author: Author of the book
        :param year: Publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor called when the object is deleted.
        Prints a message indicating the book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Informal string representation for the user.
        :return: A readable string with book details.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation for developers.
        Should ideally return a string that can recreate the object.
        :return: A recreatable representation of the book.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
