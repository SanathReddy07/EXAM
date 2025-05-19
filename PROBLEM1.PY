class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Cannot divide by zero"
        return self.a / self.b
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()

calc = Calculator(a, b)

if operation == "add":
    print("Result:", calc.add())
elif operation == "subtract":
    print("Result:", calc.subtract())
elif operation == "multiply":
    print("Result:", calc.multiply())
elif operation == "divide":
    print("Result:", calc.divide())
else:
    print("Invalid operation")
