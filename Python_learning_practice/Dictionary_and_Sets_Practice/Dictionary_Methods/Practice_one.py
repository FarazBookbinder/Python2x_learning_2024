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
# dict_with_list = {
#     "Name": "Faraz",
#     "Surname": "",
#     "Subjects": ["Maths", "Physics", "Chemistry", "Biology"],
#     "Birth_State": "Gujarat",
#     "Birth_City": "Ahmedabad",
#     "Is_adult": True
# }
# print(dict_with_list["Name"])
# print(dict_with_list["Surname"])
# print(dict_with_list["Subjects"])
# print(dict_with_list["Birth_State"])
# print(dict_with_list["Birth_City"])
# print(dict_with_list["Is_adult"])

# Assign the different value to the key and also add the new key value pair.
dict_with_list = {
    "Name": "Faraz",
    "Subjects": ["Maths", "Physics", "Chemistry", "Biology"],
    "Birth_State": "Gujarat",
    "Birth_City": "Ahmedabad",
    "Is_adult": True
}
print(dict_with_list)
dict_with_list["Name"] = "Omair"
dict_with_list["Surname"] = "Vora"
dict_with_list["Birth_State"] = "Telangana"
dict_with_list["Birth_City"] = "Hydrabad"
dict_with_list["Is_adult"] = False
dict_with_list["Surname"] = "Bookbinder" #Add this line as a new key value pair
print(dict_with_list)
