# with open("practice.txt", "w") as file:
#     file.write("Hi Everyone\nWe are learning file I/O\nUsing Java\nI like Programming in Java.")
#
# with open("practice.txt", "r") as file:
#     data = file.read()
#
# new_data = data.replace("Java", "Python", 2)
# print(new_data)
#
# with open("practice.txt", "w") as file:
#     file.write(new_data)

# WAP to search if the word "Learning" is exist in the file or not.

word = "Xlearning"
with open("Practice.txt", "r") as file:
    data = file.read()
    if data.find(word) != -1:
        print("Found")
    else:
        print("Not Found")

