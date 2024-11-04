# # Sets are immutable
# # in the sets ignord the duplicate value.
#
# my_collection = {10,2,3,4,5,6,9,0}
# print(my_collection)
#
# # type casting of the set to list
# new_collection = list(my_collection)
# print(new_collection[7])
#
# # Program to use the duplicate value and observ the output
# collection_new = {1, 1, 2, 3, 4, 5, 5, 7, 7, "Faraz", "Omair", "Afrin", "Faraz", "faraz"}
# print(collection_new)
# print(len(collection_new))
#
# # How to create a empty set
# set_new = ()
# # here not use curly brace because curly brace is also use for the dictionary that's why.

my_set = {9,9.0}
print(my_set)
# As above python consider 9 or 9.0 as same value

# Now solution as follows:-
my_set1 = {9,"9.0"}
print(my_set1)

#Another solution as follows:-
my_set2 = {
    ("int", 9),
    ("float", 9.0)
}
print(my_set2)