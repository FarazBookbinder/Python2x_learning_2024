number1 = int(input("Please enter the number 1:-"))
number2 = int(input("Please enter the number 2:-"))
number3 = int(input("Please enter the number 3:-"))

if number1 >= number2 and number1 >= number3:
    print("greatest number is", number1)
elif number2 >= number1 and number2 >= number3:
    print("Greatest number is", number2)
else:
    print("Greatest number is", number3)
