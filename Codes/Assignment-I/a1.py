#Assignment 1:
#Problem Statement:

# You are tasked with implementing a simple library system using Python classes. 
# Create a Book class with encapsulated attributes for the book's title, author, and ISBN. 
# Include methods to display book information and check if the book is available or checked out. 
# Create an object of the Book class and demonstrate its functionality.

class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._checked_out = False

    def display_info(self):
        return f"Title: {self._title}\nAuthor: {self._author}\nISBN: {self._isbn}\nChecked Out: {'Yes' if self._checked_out else 'No'}"

    def check_out(self):
        if not self._checked_out:
            print(f"The book '{self._title}' is now checked out.")
            self._checked_out = True
        else:
            print("Sorry, the book is already checked out.")

    def check_in(self):
        if self._checked_out:
            print(f"The book '{self._title}' has been checked in.")
            self._checked_out = False
        else:
            print("The book is not currently checked out.")

# Create a Book object
book1 = Book("The Python Programming Language", "Guido van Rossum", "978-0-596-15810-1")

# Demonstrate functionality
print(book1.display_info())
book1.check_out()
print(book1.display_info())
book1.check_in()
print(book1.display_info())




