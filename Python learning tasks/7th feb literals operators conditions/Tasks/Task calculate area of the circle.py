import math
# Write a Python program to calculate the area of a circle given its radius using the
# formula area=π×r^2 ( Take pie as 3.14)
# A = pi r2
"""
radius = int(input("Enter the radius of the circle:-"))
area = 3.14 * radius * radius
print("Area of the circle is:-", area)
"""
"""
#Another Approach
radius = int(input("Enter the radius of the circle:-"))
area = (3.14 * (radius ** 2))
print("Area of the circle is:-",area)
"""
#Another Approach
radius = int(input("Enter the radius of the circle:-"))
area = math.pi * pow(radius, 2)
print("Area of the circle is:-",area)
