"""
Module 3: Object-Oriented Programming in Python
------------------------------------------------
This script provides an in-depth understanding of OOP concepts:
1. Classes
2. Objects
3. Methods
4. Inheritance
5. Encapsulation
6. Polymorphism
Each section includes explanations and examples.

Additionally, a practical application for a construction company is provided.

The script also demonstrates:
- Writing reusable functions
- Importing and using Python libraries
- File Handling (Reading and Writing to Files)
"""

import math  # Example of importing a built-in Python library

# 1. Classes and Objects
print("\n=== Classes and Objects ===")


class ConstructionProject:
    """A class representing a construction project."""

    def __init__(self, name, location, budget):
        self.name = name  # Attribute
        self.location = location  # Attribute
        self.budget = budget  # Attribute

    def display_project_info(self):
        """Method to display project details."""
        print(f"Project: {self.name}, Location: {self.location}, Budget: ${self.budget}")


# Creating an object
project1 = ConstructionProject("Mall Construction", "Downtown", 500000)
project1.display_project_info()

# Practical Application: File Handling in Construction Company
print("\n=== File Handling ===")

# Writing data to a file
with open("construction_data.txt", "w") as file:
    file.write("Construction Materials Inventory:\n")
    for material, quantity in materials.items():
        file.write(f"{material}: {quantity} units\n")
    file.write("\nTotal Material Cost: $" + str(total_cost) + "\n")

print("Data has been written to construction_data.txt")

# Reading data from a file
with open("construction_data.txt", "r") as file:
    print("\nReading from file:")
    content = file.read()
    print(content)

# Managing materials inventory using a dictionary
materials = {
    "cement": 500,  # bags
    "sand": 1000,  # kg
    "bricks": 2000,  # pieces
    "steel rods": 150  # units
}
print("Construction Materials:", materials)

price_per_unit = {
    "cement": 10,  # Price per bag
    "sand": 5,  # Price per kg
    "bricks": 2,  # Price per piece
    "steel rods": 15  # Price per unit
}


def calculate_material_cost(materials, price_per_unit):
    """Reusable function to calculate material costs."""
    total_cost = 0
    for material, quantity in materials.items():
        cost = quantity * price_per_unit.get(material, 0)
        total_cost += cost
        print(f"Cost for {material}: {cost}")
    return total_cost


# Using the reusable function
total_cost = calculate_material_cost(materials, price_per_unit)
print("Total Material Cost:", total_cost)
