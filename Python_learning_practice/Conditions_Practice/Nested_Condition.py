age = int(input("Please Enter your age:-"))
if age >= 18:
    if age >= 75:
        print("Hello Oldies.. You are not allow to drive the vehicle.")
    else:
        print("Congrats!! you are allow to drive a vehicle.")
else:
    print("Sorry!! You are not allow to drive the vehicle. Your age is just", age)
