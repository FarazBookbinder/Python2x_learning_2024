# my_new_set = set()
# my_new_set.add((1, 2, 3, 4))
# my_new_set.add("World")
# print(my_new_set)

#my_new_set.add([1, 2, 3, 4])
#print(my_new_set)
#my_new_set.add({"name": "Faraz"})
#print(my_new_set)

# Line no 5 to 8 not execute because in python set elements are immutable.
# and here we use list and sets so both are mutable.

set_add = set()
set_add.add(("a", 1, 2, "v", "y", 4))
print(set_add)
new_set = {9, 9, 6, "Faraz"}
set_add.add(new_set)
print(new_set)
