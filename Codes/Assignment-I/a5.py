# Assignment 5:
# Problem Statement:
# Create a Python class named Student with the following attributes and methods:

# Attributes: name, age, grade
# Methods:
# __init__(self, name, age): Initializes the name, age, and sets grade to an initial value.
# set_grade(self, grade): Sets the grade of the student.
# get_details(self): Returns a string containing the details of the student (name, age, grade).

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = "N/A"

    def set_grade(self, grade):
        self.grade = grade

    def get_details(self):
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Example usage:
student1 = Student("Alice", 18)
student1.set_grade("A")
print(student1.get_details())
