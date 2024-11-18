# How to define functions
def sum_of_numbers(a, b):
    sum = a + b
    print(sum)
    return sum


sum_of_numbers(1, 3)


# Another Way...
def calc_sum(x, y):
    return x + y


calc = calc_sum(4, 6)
print(calc)


# simple function without parameters

def print_hello():
    print("Hello")


print_hello()
print_hello()


# Average of any 3 numbers from the user input using functios
def average_of_three_number():
    x = int(input("Please enter the first value: "))
    y = int(input("Please enter the second value: "))
    z = int(input("Please enter the third value: "))
    addition = x + y + z
    average = addition / 3
    print("The average is: ", average)
    return average

average_of_three_number()
average_of_three_number()
average_of_three_number()

