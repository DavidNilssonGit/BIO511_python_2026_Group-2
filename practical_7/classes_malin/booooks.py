class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = False
        self.borrower = None

    def __str__(self):
        # The __str__ dunder method will be called when using print(book_obj)
        return f"'{self.title}' by {self.author} ({self.year})" # information about the book


class Library:
    def __init__(self): 
        self.books = []
        self.available_books = [] #list of avalible books
    def add_book(self, book):
        self.books.append(book) #add books in list
        book.available = True #gör bok tillgänglig
        self.available_books.append(book)


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    def borrow_book(self, library, book):#member can borrow book
        if book.available:
            print(f"{self.name} borrowed {book.title}!")
            book.available = False # book not available
            book.borrower = self #who borrowed book
            self.borrowed_books.append(book) #member list
            library.available_books.remove(book) # removes book from list
        else:
            print("Book not available")


# Example usage
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("Dune", "Frank Herbert", 1965)
book4 = Book("The Hitchhiker's Guide to the Galaxy","Douglas Adams", 1979)
library = Library()
library.add_book(book1)  # Should add book1 to the library and make it available for borrowing
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
member1 = Member("Battle Ass")
member2 = Member("Ankefar")
member1.borrow_book(library, book1)  # Now the book should be borrowed by Alice
member2.borrow_book(library, book2)
print("Available books:", [str(book) for book in library.available_books])
