# in python we have try and except block to handle the exceptions cases.
# What is the meaning of exception? :- When errors interrupt the flow of the program at the point where they appear,-
# so any further code stops executing.

x = int(input("Please enter the value 1 for the divide\n"))
y = int(input("Please enter the value 2 for the divide\n"))

try:
    result = x/y
    print("Your result is:-", result)
except Exception as e:
    print("This error occur because you enter the value which like divide by 0", e)
print("Thanks..")