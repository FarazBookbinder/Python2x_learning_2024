#Condition 1
age = int(input("Please Enter Your Age:-"))
if age >= 18:
    print("You are good to go to Pub")
else:
    print("Sorry Buddy We are not allow you.")

#condition 2
age = 17
if age == 18:
    print("You are good to go to Pub")
else:
    print("Sorry Buddy We are not allow you.")

#Condition 3
x = int(input("Please enter your value1:-"))
y = int(input("Please enter your value2:-"))
if x > y:
    print("You are the one good to go")
elif x < y:
    print("I am with you go...")
elif x == y:
    print("Try again")