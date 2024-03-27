#Tuple is collection of items
#Rule :- Tuple is immutable.

my_list = [6, 7, 8, 9, 10]
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

#list convert to tuple
new_tup = tuple(my_list)
print(new_tup)
print(my_list)

#Tuple Convert to list
the_tup = (90, 91, 92)
print(list(the_tup))

#How we can write tuplw
tuple1  = ()
tuple2 = (1, 2, 3, 4)
tuple3 = (["Apple", 400, "Banana", 150])

print(tuple1)
print(tuple2)
print(tuple3)

"""
del tuple3
print(list(tuple3))
"""

# Concatination of tuples
tuple_data1 = (1, 2, 3, 4, 5)
tuple_data2 = (6, 7, 8, 9, 10)
tuple_conct = tuple_data1 + tuple_data2
print(tuple_conct)

# Multiple assignment in python
a,b,c = (89, 91, 93)
print(a,b,c)

#Nested Tuple
tuple_data1 = ("Faraz", "Aafi", "Omair")
tuple_data2 = ("Farooque","Najma")
family_member = (tuple_data1,tuple_data2)
print(family_member)
print(family_member[0][2])
print(family_member[1][0])

#search in to the tuple
my_accessories = ("Watch", "Wallet", "Belt", "Backpack", "Baseball Cap")
print("Belt" in my_accessories)

