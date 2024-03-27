# Poly - Many
# Morphism - Form
# means multiple class available but in all class function is same so those same function is behave differently

# 2 concept of Polymorphism
# 1. Method Overloading
# 2. Method Overriding

class Shape:
    def area(self):
        print("Area of the shape is:-")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shape1 = Rectangle(12,10)
print(shape1.area())

shape2 = Circle(12)
print(shape2.area())

shape3 = Shape()
print(shape3.area())
