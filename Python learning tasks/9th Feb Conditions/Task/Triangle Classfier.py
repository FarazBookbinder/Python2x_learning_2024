side1 = int(input("PLease enter the length of side 1:-"))
side2 = int(input("PLease enter the length of side 2:-"))
side3 = int(input("PLease enter the length of side 3:-"))
if side1 == side2 == side3:
    print("This is the equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is the  isosceles triangle")
else:
    print("This is scalene triangle")