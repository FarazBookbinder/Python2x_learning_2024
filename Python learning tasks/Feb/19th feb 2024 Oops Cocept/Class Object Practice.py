# Question:- What is self in method?
# Answer:- self is the reference to access the variable.
#Class :- Car
#Object :- Tesla, Lamborgini

class Car:
    name = None
    color = None
    type = None
    model = None
    engine_type = None

    def car_name(self):
        print("Car name is:-" + self.name)

    def car_color(self):
        print("Car color is:-" + self.color)

    def car_type(self):
        print("Car type is:-" + self.type)

    def car_model(self):
        print("Car model is:-" + self.model)

    def car_engine_type(self):
        print("Car engine type is:-" + self.engine_type)


Lamborghini_obj = Car()
Lamborghini_obj.name = "Lamborghini Evantadoor"
Lamborghini_obj.car_name()
Lamborghini_obj.color = "Red"
Lamborghini_obj.car_color()


