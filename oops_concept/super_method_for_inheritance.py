class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car is started")

    @staticmethod
    def stop():
        print("Car is stopped")


class Model(Car):
    def __init__(self, year, type):
        super().__init__(type)
        self.year = year


car1 = Model("2019", "Petrol")
print(car1.year)
print(car1.type)