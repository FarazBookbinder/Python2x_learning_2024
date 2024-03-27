# *args using this user have not add the literals just put the value when calling the function.
"""
def args_progarm(*args):
    for i in args:
        print("Hello", i)

print(1,2,3,4,5)
"""
"""
# With the list
def args_fruit(*fruits):
    for i in fruits:
        print("Hello", i)
Faraz = args_fruit("Banana","Lichi","Grape")
Aafi = args_fruit("Guawa","Pinaple","Orange")
"""
# assign with args
def pizza_type(*cheeseburst,base):
    for i in cheeseburst:
        print(i,base)
    return cheeseburst, base


pizza = pizza_type("Small", "Medium", "Large", base="smooth")
print(pizza)
