scale = int(input("Please enter your marks:-"))
if scale >= 90 and scale <= 100:
    print("Your grade is A")
elif scale >= 80 and scale <= 89:
    print("Your grade is B")
elif scale >= 70 and scale <= 79:
    print("Your grade is C")
elif scale >= 60 and scale <= 69:
    print("Your grade is D")
elif scale >= 50 and scale <= 59:
    print("Your grade is E")
elif scale >= 1 and scale <= 49:
    print("Your grade is E")
else:
    print("Please Enter a Valid Number..")