# Reading a file in python
# Able to read specific length of character in the file.
# file = open("Demo.txt", "r")
# data = file.read(15)
# print(data)
# file.close()

# Able to print the line one by one
file = open("Demo.txt", "r")
data = file.readline()
print(data)
data1 = file.readline()
print(data1)
data2 = file.readline()
print(data2)
data3 = file.readline()
print(data3)
data4 = file.readline()
print(data4)


file.close()