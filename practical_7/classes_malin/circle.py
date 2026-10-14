class Circle:
    def __init__(self, radius): # Initializes the circle with a radius
        self.radius = radius

    def calc_perimeter(self): # Calculates and returns the circumference(omkrets)
        return 2 * 3.14 * self.radius

    def calc_area(self): # Calculates and returns the area
        return 3.14 * self.radius ** 2

my_circle = Circle(4)
print(my_circle.calc_perimeter())
print(my_circle.calc_area())