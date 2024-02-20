#Question:- What is set?
#Answer:- Set is a un-orderd unique items.

# Simple set-------
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9}
print(set1)

seti = {"Faraz", "Omair", "Afrin", "Najma", "Farooque", "Faraz"}
print(seti)

#Convert list to set--------
list11 = [45.29, 33, 33, 45, 21]
setx = set(list11)
print(setx)
print(list11)

#Union with the set.
seta = {1, 2, 3, 4, 4}
setb = {5, 6, 7, 8, 9, 9}
set_a_and_b = seta.union(setb)
print(set_a_and_b)

#Intersection with the set. Inter preter gives common data as a result
seta = {1, 2, 3, 4, 4, 5}
setb = {5, 6, 7, 8, 9, 9, 3, 1}
set_a_and_b = seta.intersection(setb)
print(set_a_and_b)

#Difference with the set.
seta = {1, 2, 3, 4, 4, 5}
setb = {5, 6, 7, 8, 9, 9, 3, 1}
set_a_and_b = seta.difference(setb)
set_a_and_b_comb = setb.difference(seta)
print(set_a_and_b)
print(set_a_and_b_comb)

# Subset
set_new_1 = {1, 2, 3, 4, 4}
set_new_2 = {1, 2, 3, 4, 4}
set_new_result = set_new_1.issubset(set_new_2)
print(set_new_result)

# Set with loop
set_use_1 = {1, 2, 3, 4, 5, 6, 6, 5, 4, 1}

for i in set_use_1:
    print(i)


# Practice of set
set_full_1 = {1, 2, 3, 4, 5, 6, 7, 8, 20}
print(set_full_1)
set_full_1.remove(5)
print(set_full_1)
print(len(set_full_1))