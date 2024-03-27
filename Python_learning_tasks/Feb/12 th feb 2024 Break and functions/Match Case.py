numbers = int(input("Please enter the number in 1 to 4\n"))
match numbers:
    case 1:
        print("You have entered number 1")
    case 2:
        print("You have entered number 2")
    case 3:
        print("You have entered number 3")
    case 4:
        print("You have entered number 4")
    case _:
        print("This numer is out of range")

# Break is not needed in Match case