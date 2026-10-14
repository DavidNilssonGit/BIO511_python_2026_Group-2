# Part 1: Write a new class, starting with the keyword "class"
# Give the new class a set of attributes

class MyFruit:
    def __init__(self, type, colour, origin):
        self.type = type
        self.colour = colour
        self.origin = origin

# Create some new objects

fruit1 = MyFruit("apple", "red", "Sweden")
fruit2 = MyFruit("banana", "yellow", "Spain")

# Print object with its attributes
# Each request for object and attribute needs to be written separately

print(fruit1.type)
print(fruit1.colour)
print(fruit1.origin)

# Part 2: Working with methods
# Create a calculator class
# Class should include addition, subtraction and multiplication

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
print(my_calc.add())
print(my_calc.subtract())
print(my_calc.multiply())


# Write a class "Circle" with the attribute "radius"

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimiter(self):
        return self.radius * 2 * 3.14

    def area(self):
        return self.radius ** 2 * 3.14

radius = float(input("Enter the radius of the circle: "))
my_circle = Circle(radius)

print(my_circle.perimiter())
print(my_circle.area())


# Part 3: Classes/objects within classes


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = False
        self.borrower = None

    def __str__(self):
        # The __str__ dunder method will be called when using print(book_obj)
        return f"Informative message about the book. You can also use attributes {self.title}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        book.available = True

    def borrow_book(self, book, member):
        if book in self.books and book.available
            book.available = False
            book.borrower = member.name 

        

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


# Example usage
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
library = Library()
library.add_book(book1)  # Should add book1 to the library and make it available for borrowing
member1 = Member("Alice")
member1.borrow_book(library, book1)  # Now the book should be borrowed by Alice
print("Available books:", [str(book) for book in library.available_books])

