# Assignment 3:
# Problem Statement:

# Implement a Student class with encapsulated attributes for a student's name, roll number, and grades. Include a method to calculate the average grade and display the student's information. Create an object of the Student class and demonstrate its functionality.

class Student:
    def __init__(self, name, roll_number, grades):
        self._name = name
        self._roll_number = roll_number
        self._grades = grades

    def calculate_average_grade(self):
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)

    def display_info(self):
        return f"Name: {self._name}\nRoll Number: {self._roll_number}\nGrades: {', '.join(map(str, self._grades))}\nAverage Grade: {self.calculate_average_grade()}"

# Create a Student object
student1 = Student("Alice Smith", "2021001", [90, 85, 92, 88, 95])

# Demonstrate functionality
print(student1.display_info())
