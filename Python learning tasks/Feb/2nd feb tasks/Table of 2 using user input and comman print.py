# Simple approach

num = 2
print(f"{num}x1={num*1}")
print(f"{num}x2={num*2}")
print(f"{num}x3={num*3}")
print(f"{num}x4={num*4}")
print(f"{num}x5={num*5}")
print(f"{num}x6={num*6}")
print(f"{num}x7={num*7}")
print(f"{num}x8={num*8}")
print(f"{num}x9={num*9}")
print(f"{num}x10={num*10}")


# Using loop
"""
num = int(input("Please enter the table number:-"))
for i in range(1, 11):
    result = (num*i)
    print(f"{num} x {i} = {result}")


logic:-

num = int(input("Please enter the table number: ")): 
This line prompts the user to enter a number and stores it in the variable num. 
The int() function is used to convert the user input, which is initially a string, into an integer.

for i in range(1, 11):: 
This line sets up a loop that will iterate 10 times, with i taking on values from 1 to 10.

result = num * i: 
Inside the loop, this line calculates the result of multiplying 
the user-entered number (num) by the current value of i.

print(f"{num} x {i} = {result}")
This line uses an f-string to print the multiplication table in a readable format. 
It includes the original number entered by the user (num), the current value of i, 
and the result of the multiplication (result).
"""