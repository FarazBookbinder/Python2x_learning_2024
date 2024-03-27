import math
class Calculator:
    def sum(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mult(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b

calc = Calculator()
result = calc.sum(6,9)
print(result)
result = calc.sub(6,9)
print(result)
