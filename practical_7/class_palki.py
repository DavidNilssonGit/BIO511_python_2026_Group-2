'''
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")


book1 = Book("1984", "George Orwell", 1949)
book1.display()

book2 = Book("Dystopian", "George Orwell", 1949)
book2.display()

book3 = Book("cooking", "Georgia", 1947)
book2.display()

###############################################

class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

    def details(self):
        return f"{self.name}, Age: {self.age}"

Patient1 = Patient("445678", "Ana", "56")
print(Patient1.details())

Patient2 = Patient("445648", "Ara", "69")
print(Patient2.details())

##############################################


class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2


my_calc = Calculator(4, 6)

print(my_calc.add())       # 10
print(my_calc.subtract())  # -2
print(my_calc.multiply())  # 24

###############################################


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.perimeter = 2 * math.pi * radius
        self.area = math.pi * radius**2

r = float(input("Enter radius: "))

circle = Circle(r)

print(circle.radius)
print(circle.perimeter)
print(circle.area)



###############

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_perimeter(self):
        return 2 * 3.14 * self.radius

    def calc_area(self):
        return 3.14 * self.radius**2


r = float(input("Enter radius: "))

circle = Circle(r)

print("Radius:", circle.radius)
print("Circumference:", circle.calc_perimeter())
print("Area:", circle.calc_area())

####################################################
'''

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = False
        self.borrower = None

    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrower}"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        book.available = True
        self.books.append(book)

    @property
    def available_books(self):
        return [book for book in self.books if book.available]


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, book):
        if book not in library.books:
            print(f"{book.title} is not in the library.")
        elif not book.available:
            print(f"{book.title} is already borrowed.")
        else:
            book.available = False
            book.borrower = self.name
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            book.borrower = None
            print(f"{self.name} returned {book.title}")

    def __str__(self):
        return f"Member: {self.name}, Borrowed books: {len(self.borrowed_books)}"


# Example usage
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

library = Library()
library.add_book(book1)
library.add_book(book2)

member1 = Member("Alice")
member2 = Member("Bob")

member1.borrow_book(library, book1)
member2.borrow_book(library, book1)  # should fail

print("Available books:")
for book in library.available_books:
    print(book)

member1.return_book(book1)

print("\nAvailable books after return:")
for book in library.available_books:
    print(book)