# A dictionary is a un-Ordered collection of data in a key value pair.
my_dict = {"Faraz": 7048182616, "Aafi": 1234567890, "Omair": 2104202209}
print(my_dict["Faraz"])
print(my_dict["Aafi"])
print(my_dict["Omair"])

# Dictionary with duplicate value.
my_rule = {"Rule1": "Daily learning", "Rule2": "Practice on this", "Rule3": "Clear doubts", "Rule1": "Keep Motivate"}
print(my_rule)
# Dictionary keys and values other way.
keys = my_rule.keys()
print(keys)

keys_value = my_rule.values()
print(keys_value)

keys_list = list(keys)
print(keys_list)

#Get the student data using the Dictionary and  function

def get_student_details(name, age, grade):
    student_info = {"Name": name, "Age": age, "Grade": grade}
    return student_info

student1 = get_student_details("Omair",18,10)
print(student1)

student2 = get_student_details("Faraz",19,9)
print(student2)

#Dictionary using the .get.

my_1st_dict = {"Name":"Faraz", "Mobile Number": 9090898909, "State": "Gujarat", "180051": "zip"}
print(my_1st_dict.get("180051")) # If we use .get then must be use proper value if it's "String" then use""

# Dictionary using .pop function
my_key = {"Name": "Faraz", "Age": 29, "Education": "BE IT"}
final_list = my_key.pop("Name")
print(final_list)

# Dictionary iterate over the list using for loop
family = {"Faraz": "The musketeers", "Afrin": "The Better Half", "Omair": "Is God Gift"}
print(family)
for k,v in family.items():
    print(k,"-",v)

#Found the key is exist or not.
found_dictionary = {"a": 1, "b": 10, "c": 5}
for k,v in found_dictionary.items():
    if k == "b":
        print("b is found")
    elif v == 10:
        print("10 is available")
    if k == "a":
        print("a is available")
    elif v == 1:
        print("1 is available")
    if k == "c":
        print("c is available")
    elif v == 5:
        print("5 is available")