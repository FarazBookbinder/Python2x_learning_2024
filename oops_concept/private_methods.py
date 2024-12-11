# Private methods is only accessible in the cass not outside the class.

class Students:
    def __init__(self, name):
        self.name = name

    def __result(self):
        print("Your name is:", self.name)

    def final_result(self):
        print(self.__result())
    
c1 = Students("Faraz")
print(c1.name)
# print(c1.__result)
print(c1.final_result())

# So how to call the private methods? for this check the line number 10, 11, 16 in above code.