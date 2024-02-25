#class - Attributes(Data member) and Behaviour-(Methods)(Member function).
#Functions:- Functions are not use in the classes.

class person:
    name = None
    age = None
    mobile = None
    height = None
    weight = None

#Now Below is the methods because methods are the part of classes.
    def is_walk(self):
        print("I am able to talk.")

    def is_sleep(self):
        print("I am able to sleep.")

    def is_eat(self):
        print("I am able to eat.")

    def is_think(self):
        return "I am able to think"

#Create object as below
faraz = person()
faraz.name = "My name is Faraz"
faraz.height = "My height is 6.2ft"
print(faraz.name, "\n", faraz.height)

omair = person()
omair.name = "My name is Omair"
omair.height = "My height is 2ft"
print(omair.name, "\n", omair.height)