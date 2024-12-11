# Private attributes is only accessible in the cass not outside the class.

class students:
    def __init__(self, name, subjects):
        self.__name = name
        self.__subjects = subjects

    def verification(self):
        print("hello", self.__name, "You choose",self.__subjects)

c1 = students("Faraz", "Maths")
# print(c1.__name)
print(c1.verification())

# So how to access this? for this check the above code line number 7, 8, 12
# here for to access the attribute using the another method which is not a private means internally we can call them.
