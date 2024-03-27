"""
def my_salary(num):
    return num * 2
add_salary = my_salary(100)
print(add_salary)
"""

# Practice program for mathematics operation of 2 numbers using user input
def math_is(x, y):
    return x + y, x - y, x * y


a = int(input("Please enter the number1\n"))
b = int(input("Please enter the number2\n"))
result = math_is(a, b)
print("addition/subtraction/multiplication of", a, b, "=", result)
