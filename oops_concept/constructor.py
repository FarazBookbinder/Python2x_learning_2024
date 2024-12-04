# generally we can call the constructor as __init__ function.
# Below is the example of the constructor.

# class Patient_Details:
#     def __init__(self):  # using the __init__ define he constructor function.
#         print("This is the constructor")
#
#
# s1 = Patient_Details()  # when use "()" during the creating an object then the constructor is automatically called.


# how Self is work in the constructor. also this is the parameterized constructor.

class Patient_name:
    def __init__(self, name):
        self.name = name
        print("Below is the patient name details")


c1 = Patient_name("Faraz")
print(c1.name)
c2 = Patient_name("Omair")
print(c2.name)
