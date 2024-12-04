with open("Demo.txt", "r") as file:
    data = file.read()
    print("data")

with open("Demo.txt", "w") as file:
    file.write("New Data You can Able To Add")
    print(file)
