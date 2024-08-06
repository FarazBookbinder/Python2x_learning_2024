# # range is a function which use in for loop
# my_sequence = range(10)
# for i in range(5):
#     print(i)
#
#     OR

# for i in range(5):
#     print(i)
# Range conditions is like range(start(Optional, Stopig(Must), steps(Optional))
# for i in range(2, 10):
#     print(i)
#
# print("Next is")
#
# for i in range(0, 12, 2):
#     print(i)

# Practice print the numbers from (1 to 100)
# for i in range(1, 101):
#     print(i)

# Practice print the numbers from (100 to 1)
# for i in range(100, 0, -1):
#     print(i)

# Practice print the multiplication table for the number n.
user_input = int(input("Please enter the number which you wants to do multiplication:-"))
for i in range(1, 11):
    print(f"{user_input} * {i} =", user_input * i)
    i += 1
