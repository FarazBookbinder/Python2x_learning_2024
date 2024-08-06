# i = 1
# while i <= 5:
#    print("Hello World")
#    i = i + 1

# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1

# i = 5
# while i >= 1:
#     print(i)
#     i = i - 1
# Practice Questions
# Q1:- Print the numbers from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i = i + 1

# Q2:- Print the numbers from 100 to 1.
# i = 100
# while i >= 1:
#     print(i)
#     i = i - 1

# Q3:- Print the multliplication table of number n
# multiplier = int(input("Please enter number:-"))
# counter = 1
# while counter <= 10:
#     result = counter * multiplier
#     print(f"{counter} x {multiplier} = {result}")
#     counter = counter + 1

# Q4:- Print the elements of the following list using a loop.
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list_1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(list_1):
#     print(list_1[idx])
#     idx = idx + 1

# Q5:- Search for a number x in this tuple using loop (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
tup_1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36
i = 0
found = False
while i < len(tup_1):
    if tup_1[i] == x:
        print("Value Found at", i)
        found = True
    i += 1
if not found:
    print("Entered value is not present")
