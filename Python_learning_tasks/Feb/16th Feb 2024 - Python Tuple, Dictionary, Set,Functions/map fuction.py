import math
#Double the list value Below is the way generally we use:-
s_list = [3,6,9,12,15]
d_list = []
for i in s_list:
    temp = i**2
    d_list.append(temp)
print(d_list)

#Using the function
list_value = [3, 6, 9, 12, 15]

def doub_numbers(list_value):
    return [x ** 2 for x in list_value]

print(doub_numbers(list_value))

#Now...... Using the map() function square root example as below
list_value = [3,6,9,12,15]
def doub_numbers(num):
    return num ** 2

doub_numbers_result = list(map(doub_numbers, list_value))
print(doub_numbers_result)

#Another example
numb_list = [3,6,9,12,15]
def sq_root(num):
    return math.cbrt(num)

list_numbers = [3,6,9,12,15]
sq_root_result = list(map(sq_root,numb_list))
print(sq_root_result)

# map() function created for the list,tuples,set,dictionary because this all are contains bunch of items.