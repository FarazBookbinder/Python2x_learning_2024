"""
def detail_of_house(name="Sukun Villa",number = 8):
    print("My house name is",name, "and number is", number)

detail_of_house()

#here name and number is define at the time of define function so no need to add args at the time of calling funtion.
"""
"""
def detail_of_car(name="VW Polo",year = 2019,type = "Hatchbg gt"):
    print("My car name is",name, "and year is", year, "and type is", type)

detail_of_car()
"""


# Another case is if default argument available then at the time of function call if user pass the value then
# python consider the passed value at the time of funtion calling.

def detail_of_my_computer(name="Apple mac book pro", year=2022, ram="1TB"):
    print("My PC name is", name, "and year is", year, "and ram is", ram)


detail_of_my_computer()
detail_of_my_computer("Air book pro advance","2024","1TB")
