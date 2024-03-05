class ABC:
    def f1(self):
        try:
            a = int(input("Please enter the number1\n"))
            b = int(input("Please enter the number2\n"))
            result = a + b
        except ValueError as v:
            print("Please enter the integer value only", v)
        else:
            print("Your result is:-", result)


obj1 = ABC()
obj1.f1()
