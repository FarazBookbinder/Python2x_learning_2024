# list_of_city = ["Ahmedabad", "Mumbai", "Surat", "Banglore", "Pune"]
#
# for lis in list_of_city:
#     print(lis)

# Practice
# Print the elements of the following list using a loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print("New As Below")
# list_of_nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# for list_num in list_of_nums:
#     print(list_num)

# Search the number x in tuples using loop

# tuple_num = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
# x = 29
# i = 0
# for numbers in tuple_num:
#     if numbers == x:
#         print("Number Matched You Are Welcome")
#         break
#     i += 1
# else:
#     print("Number is not matched")

# album = ["WBSS", "Thriller", "Beat It", "PYT"]
#
# for i in album:
#     print("Playing", i)


# Find the factorial of number n given by user.
# num_n = int(input("Please enter the number n"))
# facto_init = 1
# for i in range(1, num_n+1):
#     facto_init = facto_init * i
# print("Factorial is:-", facto_init)


# a = -10
# print(a)
#
# b = 20
# print(-b)

Name = "Muaaviya"
New_name = Name
print("old variable is", Name)
print("Copied variable is", New_name)
print("Memory address of old variable", id(Name))
print("Memory address of copied variable", id(New_name))

