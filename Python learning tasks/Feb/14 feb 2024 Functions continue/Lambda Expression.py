# Purpose of the lambda expression in program to short the code
# like help to convert any fuction to one line just save the length of file.

# Normal function ex:- below we have 3 line of code.
def my_salary(salary):
    return salary * 2


result = my_salary(10000)
print(result)

# Now after lambda expression code look like below.

my_salary = lambda salary: salary * 2
print(my_salary(10000))

power = lambda num: num ** 2
print(power(4))

## Multiple argument also allow
addition = lambda a, b: a + b
a = int(input("Please enter the number1:-"))
b = int(input("Please enter the number1:-"))
print(addition(a, b))
