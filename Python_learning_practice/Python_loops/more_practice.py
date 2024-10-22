# write a program to find the some of first natural numbers using while loop.
# Using while loop
# n = 11
# add = 0
# i = 1
# while i <= n:
#     add += i
#     i += 1
# print("Sum of given number is:-", add)

#Using for loop
# n = 11
# add = 0
# for i in range(1, n+1):
#      add += i
# print(f"total sum of {n} is:-", add)

# ---------------------------------------------- Next is -----------------------------------------------------
# write a program to find the factorial of n numbers using for loop.

# n = int(input("Please enter the number which you wants to find the factorial:-"))
# add = 1
# for i in range(1, n+1):
#     add *= i
#     i += 1
# print(f"Factorial of {n} is:-", add)

# write a program to find the factorial of n numbers using while loop.
n = int(input("Please enter the number which you wants to find the factorial:-"))
add = 1
i = 1
while i <= n:
    add *= i
    i += 1
print(f"Factorial of {n} is:-", add)

