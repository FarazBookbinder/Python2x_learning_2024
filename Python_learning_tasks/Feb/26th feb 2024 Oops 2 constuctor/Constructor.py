class Car:
    name = None
    make = None
    model = None
    def __init__(self, o_name, o_make, o_model): #(Constructor)Special Function it's automatically call when function is created
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def star_engine(self):
        print("Starting a car with the name"+ self.name)
        print("Starting a car with the make" + self.make)
        print("Starting a car with the model" + self.model)

starteng = Car("Tata","V6","2024")
starteng.star_engine()
print("============================================")
newstart = Car("Tesla","V6","2022")
newstart.star_engine()