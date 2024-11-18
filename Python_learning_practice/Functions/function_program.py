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

def factorial_of_number(n):
    facto_init = 1
    for i in range(1, n + 1):
        facto_init = facto_init * i
    print("Factorial is:-", facto_init)


factorial_of_number(5)


# WAF to convert USD to INR

def usd_to_inr_convert(usd_value):
    inr_value = usd_value * 83
    print(usd_value, "USD =", inr_value, "INR")

usd_to_inr_convert(3)
