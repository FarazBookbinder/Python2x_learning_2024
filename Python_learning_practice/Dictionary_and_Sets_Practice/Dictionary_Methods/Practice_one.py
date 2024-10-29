# Disctionary is mutable same as list
# dictionary is always with the key : value format
# Not able to create a duplicate key
# simple example
# dictionary_one = {"Name": "Faraz", "Surname ": "Bookbinder", "age": 30}
# print(dictionary_one)
# print(type(dictionary_one))

# Subject with the list
# dict_with_list = {
#     "Name": "Faraz",
#     "Subject": ["Maths", "Physics", "Chemistry", "Biology"],
#     "Birth_State": "Gujarat",
#     "Birth_City": "Ahmedabad"
# }
# print(dict_with_list)

# Access the single key in the tuple using below format
dict_with_list = {
    "Name": "Faraz",
    "Subject": ["Maths", "Physics", "Chemistry", "Biology"],
    "Birth_State": "Gujarat",
    "Birth_City": "Ahmedabad"
}
print(dict_with_list["Name"])
print(dict_with_list["Subject"])
print(dict_with_list["Birth_State"])
print(dict_with_list["Birth_City"])
