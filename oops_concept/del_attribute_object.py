# using del in python we are able to delete the attribute as well as object.
class students:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

s1 = students("Faraz", "Maths")
print(s1.subject)
print(s1.name)
del s1.subject
print(s1.subject)
print(s1.name)

