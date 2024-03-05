def addition():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 + num2
        print("Result: ", result)
    except ValueError as v:
        print("Invalid input! Please enter valid numbers instead of string", v)
    except Exception as e:
        print("An error occurred:", e)


addition()
