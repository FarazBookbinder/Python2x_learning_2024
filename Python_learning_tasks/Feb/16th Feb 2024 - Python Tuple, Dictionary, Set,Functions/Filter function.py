# Using this function can filter the items in the list based on logic and return the less numbers of items.

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, list_numbers)
print(list(even_numbers))

# Same using def function instead of lambda expression.

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even(num):
    return num % 2 == 0


even_numbers = filter(even, list_numbers)
print(list(even_numbers))
