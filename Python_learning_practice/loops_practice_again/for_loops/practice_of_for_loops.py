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

tuple_num = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
x = 29
i = 0
for numbers in tuple_num:
    if numbers == x:
        print("Number Matched You Are Welcome")
        break
    i += 1
else:
    print("Number is not matched")