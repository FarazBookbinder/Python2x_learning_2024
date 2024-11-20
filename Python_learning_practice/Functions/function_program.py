# WAF to print a length of a list.(List is the parameter)
# city_list = ["Chennai", "Hydrabad", "Mumbai", "Delhi", "Noida", "Pune"]
# state_list = ["Gujarat", "Rajasthan", "Maharastra", "Bunjab", "Bihar", "MP", "UP", "GOA"]
#
#
# def len_of_list(list):
#     print(len(list))
#
# len_of_list(city_list[1])
# len_of_list(state_list)

# WAF to print the elements of a list in a single line.(List is the parameter)
# fav_cars = ["Audi A8", "BMW X7", "Lamborghini Avantadoor", "Ferrari 911gt"]
#
# def fav_car_lst(list):
#     for items in list:
#         print(items, end=" ")
#
# fav_car_lst(fav_cars)

# WAF to find the factorial of n.

# def factorial_of_number(n):
#     facto_init = 1
#     for i in range(1, n + 1):
#         facto_init = facto_init * i
#     print("Factorial is:-", facto_init)
#
#
# factorial_of_number(5)


# WAF to convert USD to INR

# def usd_to_inr_convert(usd_value):
#     inr_value = usd_value * 83
#     print(usd_value, "USD =", inr_value, "INR")
#
# usd_to_inr_convert(3)

# WAF to calculate average of 2 numbers


# def calculate_average(x, y):
#     addition = x + y
#     average = addition/2
#     print("average of", x, "and", y, "is: ", average)
#     return average
#
# calculate_average(11,89)

# WAF to calculate a sum of 2 numbers and also average of 2 numbers


# def calculate_sum_and_average(a, b):
#     add = a + b
#     average = add/2
#     print(a, "and", b, "addition is: ", add)
#     print("And the average of", add, "is: ", average)
#     return add, average
#
# calculate_sum_and_average(20, 80)
# calculate_sum_and_average(100, 80)

# WAF to check the number is even or odd.

number = int(input("Please enter the number: "))


def odd_even_number_check(number):
    if number % 2 == 0:
        print(number, "EVEN")
    else:
        print(number, "ODD")
    return number

odd_even_number_check(number)