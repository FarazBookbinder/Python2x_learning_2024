class Person:
    name = None
    age = None
    no = None
    def my_details(self):
        print("Your details is", self.name, self.age, self.no)

name_is = input("Please enter your name:-\n")
age_is = input("Please enter your age:-\n")
no_is = input("Please enter your no:-\n")

obj_ref = Person()
obj_ref.name = name_is
obj_ref.age = age_is
obj_ref.no = no_is
obj_ref.my_details()
