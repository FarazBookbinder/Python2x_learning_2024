# Loops are used for the sequential traversal
# For traversing the list, String, tuples, etc.
# example 1:-
# my_list1 = [1, 2, 3, "XYZ", "ABC", 4, 5, 6, 7]
# my_list2 = ("Faraz", "Afrin", "Omair", "Najma", "Farooque")
# for i in my_list1:
#     print(i)
# else:
#     print(my_list2)

# # Example 2:-
# my_name = "Faraz Bookbinder"
# for i in my_name:
#     print(i)
# else:
#     print("Above is your name char")

# Example 3:-
# name = "MyMy"
# for i in name:
#     if i == "a":
#         print("a Found")
#         break
# else:
#     print("Value Not Found")

#Practice:-

#Practice 1:-
#Print the elements of the following list
# my_list = [1, 4, 9, 16, 25, 36, 49, 61, 81, 100]
# for i in my_list:
#     print(i)

#Practice :- 2
#search a number X using the tuple
# my_list = (1, 4, 9, 16, 25, 36, 49, 61, 81, 100)
# for i in my_list:
#     if i == 100:
#         print(f"{i} is Available")
#         break
# else:
#     print("Wrong value entered")

#Pracctice :- 3
#search a number which given by the user and it's available in the list or not
# my_list = (1, 4, 9, 16, 25, 36, 49, 61, 81, 100)
# x = int(input("Please enter the value"))
# for i in my_list:
#     if i == x:
#         print(f"Entered value is {x} and it's matched")
#         break
# else:
#     print(f"Value not found in the list")

#Practice:- 4
# search the position of the elements in the given list
# my_list = (1, 4, 9, 16, 25, 36, 49, 61, 81, 100, 4, 16)
# x = int(input("Please enter the value:-"))
# idx = 0
# for i in my_list:
#     if i == x:
#         print("Value found at index", idx)
#         break
#     idx += 1
# else:
#     print("Entered Value not available")

#                                OR

# my_list = (1, 4, 9, 16, 25, 36, 49, 61, 81, 100, 4, 16)
# x = int(input("Please enter the value: "))
# for idx, i in enumerate(my_list):
#     if i == x:
#         print("Value found at index", idx)
#         break
# else:
#     print("Entered Value not available")
