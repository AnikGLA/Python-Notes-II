# Problem Statement: Create a Python class named Library with the following features:

# The class should maintain a list of books. Each book should be an instance of the Book class with attributes such as title, author, publication_year, etc. Implement methods for adding a new book, searching for a book by title, and checking out a book (updating its availability status). Input:

# Allow the user to add multiple books by taking input for title, author, and publication year. Allow the user to search for a book by title. Allow the user to check out a book by title.

# Sample Input -

# Enter the number of books to add: 3

# Enter the title of Book 1: The Great Gatsby

# Enter the author of Book 1: F. Scott Fitzgerald

# Enter the publication year of Book 1: 1925

# Enter the title of Book 2: Pride and Prejudice

# Enter the author of Book 2: Jane Austen

# Enter the publication year of Book 2: 1813

# Enter the title of Book 3: To Kill a Mockingbird

# Enter the author of Book 3: Harper Lee

# Enter the publication year of Book 3: 1960

# Enter the title of the book to search: Pride and Prejudice

# Enter the title of the book to check out: To Kill a Mockingbird

# Sample Output -

# Book 'The Great Gatsby' added to the library.

# Book 'Pride and Prejudice' added to the library.

# Book 'To Kill a Mockingbird' added to the library.

# Book 'Pride and Prejudice' found in the library.

# Book 'To Kill a Mockingbird' checked out successfully.



class Book:
    def __init__(self, title, author, publication_year, available=True):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, publication_year):
        new_book = Book(title, author, publication_year)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        book = self.search_book(title)
        if book:
            if book.available:
                book.available = False
                print(f"Book '{title}' checked out successfully.")
            else:
                print(f"Book '{title}' is not available for checkout.")
        else:
            print(f"Book '{title}' not found in the library.")


library = Library()


num_books = int(input("Enter the number of books to add: "))
for i in range(num_books):
    title = input(f"Enter the title of Book {i + 1}: ")
    author = input(f"Enter the author of Book {i + 1}: ")
    publication_year = int(input(f"Enter the publication year of Book {i + 1}: "))
    library.add_book(title, author, publication_year)


search_title = input("Enter the title of the book to search: ")
found_book = library.search_book(search_title)
if found_book:
    print(f"Book '{search_title}' found in the library.")
else:
    print(f"Book '{search_title}' not found in the library.")


checkout_title = input("Enter the title of the book to check out: ")
library.check_out_book(checkout_title)
