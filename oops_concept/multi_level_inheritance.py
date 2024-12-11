class Car:
    Color = "Black"

    @staticmethod
    def start():
        print("Car is started..")

    @staticmethod
    def stop():
        print("Car is stopped")


class Toyota_car(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(Toyota_car):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("XUV")
print(car1.type)
car1.start()
car1.stop()
