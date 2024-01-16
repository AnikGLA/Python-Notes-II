# Assignment 4:
# Problem Statement:
# Create a Python class named Rectangle with the following attributes and methods:

# Attributes: length and width
# Methods:
# __init__(self, length, width): Initializes the length and width attributes.
# calculate_area(self): Calculates and returns the area of the rectangle.
# calculate_perimeter(self): Calculates and returns the perimeter of the rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Example usage:
rectangle1 = Rectangle(5, 8)
print(f"Area: {rectangle1.calculate_area()} square units")
print(f"Perimeter: {rectangle1.calculate_perimeter()} units")
