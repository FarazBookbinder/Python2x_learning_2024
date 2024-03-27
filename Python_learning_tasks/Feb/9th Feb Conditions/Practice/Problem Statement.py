#problem Find the max between 3 number.
"""
num1 = int(input("Please enter number 1:-"))
num2 = int(input("Please enter number 1:-"))
num3 = int(input("Please enter number 1:-"))
max_number = max(num1, num2, num3)
print(max_number)
"""
#Same using if Condition....................
num1 = int(input("Please enter number 1:-"))
num2 = int(input("Please enter number 1:-"))
num3 = int(input("Please enter number 1:-"))
if num1 > num2 and num1 > num3:
    print("max is", num1)
elif num2 > num1 and num2 > num3:
    print("max is", num2)
else:
    print("max is", num3)