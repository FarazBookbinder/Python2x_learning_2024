# Store word meaning in python dictionary
#
# my_dict ={
#     "cat": "A small animal",
#     "table": ["A piece of furniture", "List of facts & Figure"],
#     "new_table": ("A update version", "Theme based selection")
# }
# print(my_dict)

# WAP enter marks of 3 subjects from the user and store them into empty dictionary. use subject name as key and
# marks as value.

my_marks_dic = {}
maths_marks = int(input("Enter your mathematics marks:-"))
my_marks_dic.update({"Mathematics": maths_marks})
physics_marks = int(input("Enter your physics marks:-"))
my_marks_dic.update({"Physics": physics_marks})
chemistry_marks = int(input("Enter your chemistry marks:-"))
my_marks_dic.update({"Chemistry": chemistry_marks})
print(my_marks_dic)
print(type(my_marks_dic))