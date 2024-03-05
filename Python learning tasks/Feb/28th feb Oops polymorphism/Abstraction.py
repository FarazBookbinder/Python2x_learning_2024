# Hiding the details and show whenever required.

#Abstract base class
#Abstract base method

# > Abstract Method
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bow Bow")

class Cat(Animal):
    def sound(self):
        print("Meow..meow..meow..")

obj = Dog("Maxi")
obj.sound()
obj1 = Cat("Mini")
obj1.sound()