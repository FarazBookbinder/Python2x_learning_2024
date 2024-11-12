# Syntex of while loop:-
# while condition:
    # Whatever work you need to write here.

# count = 1
# while count <= 5:
#     print("Hello")
#     count += 1


# count = 5
# while count >= 1:
#     print(count)
#     count -= 1

# WAP print number from 1 to 100
# number = 1
# while number <= 100:
#     print(number)
#     number += 1

# WAP print number from 1 to 100
# number_new = 100
# while number_new >= 1:
#     print(number_new)
#     number_new -= 1

# WAP print the multiplication table of number n
# num = int(input("Please enter the number:-"))
# i = 1
# while i <= 10:
#     print(f"{num} {"*"} {i} {"="}", num * i)
#     i += 1

# print the element of the following list
# my_list = [1, 4, 8, 9, 12, 78, 99, 34, 45, 88]
# while len(my_list)-1:
#     print(my_list)
#     break
#Better way
# my_list = [1, 4, 8, 9, 12, 78, 99, 34, 45, 88]
# index = 0
# while index < len(my_list):
#     print(my_list[index])
#     index += 1

# WAP Search the number n in the following tuple.
# tup_data = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# number_by_user = int(input("Please enter your number: "))
# idx_num = 0
#
# while idx_num < len(tup_data):
#     if number_by_user == tup_data[idx_num]:
#         print("You entered", number_by_user, "and it's matched at index", idx_num)
#         break  # Exit loop if match is found
#     else:
#         print("You entered", number_by_user, "and it doesn't match at index", idx_num)
#     idx_num += 1

# Another simple program WAP to print the string while the the number is <=3
# string_value = "Muaaviya"
# i = 1
#
# while i <= 3:
#     print("My name is", string_value)
#     i += 1
# WAP to print the multiple of 7 in 1to100

# multiple_of_7 = []
# num = 1
#
# while num <= 100:
#     if num % 7 == 0:
#         multiple_of_7.append(num)
#     num += 1
#
# print(multiple_of_7)

# WRP to print a fibonacci series till 50.
# a = 0
# b = 1
# fibonacci_sequence = []
# fibonacci_till = 10
# i = 0
#
# while i < fibonacci_till :
#     fibonacci_sequence.append(a)
#     a, b = b, a + b
#     i += 1
# print(fibonacci_sequence)
#
# # Another way is
# a, b = 0, 1
# while b <= 55:
#     print(b)
#     a, b = b, a + b
# print("Done")

# Another Way
a = 0
b = 1
fibonacci_sequence = []
fibonacci_till = 10
i = 0

while i < fibonacci_till:
    fibonacci_sequence.append(a)
    temp = a # here temp = 0
    a = b    # here update a now a = b means a = 1
    b = temp + b # here update the b means b = o + 1
    i += 1
print(fibonacci_sequence)




