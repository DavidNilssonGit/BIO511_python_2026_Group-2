
class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        print(self.number1 + self.number2)

    def subtract(self):
        print(self.number1 - self.number2)

    def multiply(self):
        print(self.number1 * self.number2)

my_calc = Calculator(4, 6)
my_calc.add()
my_calc.subtract()
my_calc.multiply()