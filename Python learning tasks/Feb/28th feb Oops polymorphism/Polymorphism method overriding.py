# Python does not support method overloading by default, but you can achieve similar-
# functionality by using variable arguments or default arguments, or by using different method names.

class OverloadDemo:

    def my_method(self, a=10, b=20, c=30):
        print("Method with one parameter:", a)
        print("Method with one parameter:", b)
        print("Method with one parameter:", c)


"""
    def my_method(self, a, b)
        print("Method with two parameters:", a, b)

    def my_method(self, a, b, c):
        print("Method with three parameters:", a, b, c)
"""

# Instantiate the class
demo = OverloadDemo()
demo.my_method()
