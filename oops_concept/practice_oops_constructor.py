# Create a student class that takes name and marks of 3 subjects as argument in constructor then
# create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello World")

    def get_average(self):
        total = sum(self.marks)  # Calculate the total of marks
        average = total / len(self.marks)  # Calculate the average
        print("Hi", self.name, "Your average score is:", average)

s1 = Student("Faraz", [99, 98, 97, 88])
s1.get_average()
s1.hello()


