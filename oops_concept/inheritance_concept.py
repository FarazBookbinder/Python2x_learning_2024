# This is the single level inheritance

class Car:
    color = "Black"

    @staticmethod
    def start():
        print("Car is Started..")

    @staticmethod
    def stop():
        print("Car is Stopped..")


class Toyotacar(Car):
    def __init__(self, name):
        self.name = name


car1 = Toyotacar("Fortuner")
print(car1.name)
print(car1.color)
print(car1.start())
print(car1.stop())
