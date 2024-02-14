number = int(input("Please enter the number\n"))
if number < 0:
    print("This number is not possible")
elif number == 0:
    print("fact", 1)
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
print("fact -",fact)