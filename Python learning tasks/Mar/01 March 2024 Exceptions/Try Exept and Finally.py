# Try Except and Finally
# What if user use the value in string instead of int and also a vise versa too.
# different types of error so check.

try:
    x = int(input("Please enter the value 1 for the divide\n"))
    y = int(input("Please enter the value 2 for the divide\n"))
    result = x / y
except ValueError as v:
    print("PLease use the number instead of value error type is", v)
except ZeroDivisionError as z:
    print("This error occur because you enter the value which like divide by 0", z)
else:
    print("Your Result is:-", result)
finally:
    print("I ll be execute any how")
print("Thanks..")
