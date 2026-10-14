# Write a new class, starting with the keyword "class"
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