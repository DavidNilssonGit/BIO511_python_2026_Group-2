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

