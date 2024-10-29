from typing import List

#list1 = ["Faraz", 30, "Afrin", 29, "Omair", 2.2, "Najma", 61, "Farooque", 71.5]
# print(type(list1))
# print(list1)
# list1[9] = 67.5
# print(list1)
# print(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5], list1[6], list1[7], list1[8], list1[9])
# list1.append("Allah")
# print(list1)
# list1.sort(key=lambda v: (isinstance(v, str), v))
# print(list1)
# list1.reverse()
# print(list1)
# list1.insert(0, "Muaaviya")
# print(list1)
# list1.pop(0)
# print(list1)

# Practice:-


# Using append method.
# movies = []
# movie_list1 = str(input("Please enter your 1st favorite movie name:-"))
# movie_list2 = str(input("Please enter your 2nd favorite movie name:-"))
# movie_list3 = str(input("Please enter your 3rd favorite movie name:-"))
# movies.append(movie_list1)
# movies.append(movie_list2)
# movies.append(movie_list3)
# print(movies)

# Another way
# movies = []
# movies.append(str(input("Please enter your 1st favorite movie name:-")))
# movies.append(str(input("Please enter your 2nd favorite movie name:-")))
# movies.append(str(input("Please enter your 3rd favorite movie name:-")))
# print(movies)

# Palindrome program
# WAP list contains a palindrome
given_name = []
given_name.append(str(input("Please enter the element1:-")))
given_name.append(str(input("Please enter the element2:-")))
given_name.append(str(input("Please enter the element3:-")))
print(given_name)
name_list = given_name.copy()
name_list.reverse()
if name_list == given_name:
    print("This is the palindrome")
else:
    print("This is not a palindrome")
