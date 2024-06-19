import copy
"""
my_list1 = [1, 2, 1]

list1_copy = my_list1.copy()
list1_copy.reverse()

if my_list1 == list1_copy:
    print("It's Palindrome")
else:
    print("Not a palindrome")
"""
# User input
input1 = input("Please enter your 1st value:-")
input2 = input("Please enter your 2nd value:-")
input3 = input("Please enter your 3rd value:-")

my_list = [input1, input2, input3]
print("You entered",my_list)
my_new_copy = my_list.copy()
my_new_copy.reverse()

if my_list == my_new_copy:
    print("Your value pattern is palindrome")
else:
    print("Your value pattern is not a palindrome")

