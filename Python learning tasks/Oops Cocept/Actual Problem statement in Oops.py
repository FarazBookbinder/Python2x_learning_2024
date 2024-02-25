class students:
    name = None
    age = None
    Phone_number = None

    def watch_recordings(self):
        print("Wath Recordings")

    def do_coding(self):
        print("Do Coding questions")

    def do_assignments(self):
        print("Do Assignments")


class Course:
    def initial(self, name, code, instructor, students=None):
        self.name = name  # Name of the course
        self.code = code  # Course code or identifier
        self.instructor = instructor  # Instructor of the course
        self.students = []  # List of enrolled students

    def add_student(self, student):
        self.students.append(student)  # Add a student to the course

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)  # Remove a student from the course

    def get_students(self):
        return self.students  # Return the list of enrolled students

    def get_course_info(self):
        return f"Course: {self.name}, Code: {self.code}, Instructor: {self.instructor}"
