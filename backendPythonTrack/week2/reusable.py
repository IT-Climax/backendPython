"""
Module 2: Data Structures in Python
------------------------------------
This script provides an in-depth understanding of Python data structures:
1. Lists
2. Tuples
3. Dictionaries
4. Sets
Each section includes explanations and examples.

Additionally, a practical application for a construction company is provided.

The script also demonstrates:
- Writing reusable functions
- Importing and using Python libraries
"""

import math  # Example of importing a built-in Python library


def calculate_material_cost(materials, price_per_unit):
    """
    A reusable function to calculate total material cost.
    :param materials: Dictionary containing material quantities.
    :param price_per_unit: Dictionary containing price per unit of materials.
    :return: Total cost of materials.====
    """
    total_cost = 0
    for material, quantity in materials.items():
        total_cost += quantity * price_per_unit.get(material, 0)
    return total_cost


# 1. LISTS: Ordered, mutable collections
print("\n=== Lists ===")
fruits = ["apple", "banana", "cherry", "date"]  # Defining a list
print("Fruits List:", fruits)

# Accessing elements
print("First fruit:", fruits[0])  # Indexing
print("Last fruit:", fruits[-1])  # Negative indexing

# Modifying lists
fruits.append("elderberry")  # Adding an element
print("After append:", fruits)
fruits.remove("banana")  # Removing an element
print("After remove:", fruits)

# Looping through a list
for fruit in fruits:
    print("Fruit:", fruit)

# List comprehension
squared_numbers = [x ** 2 for x in range(5)]
print("Squared numbers:", squared_numbers)

# 2. TUPLES: Ordered, immutable collections
print("\n=== Tuples ===")
coordinates = (10.5, 20.3)  # Defining a tuple
print("Coordinates:", coordinates)

# Accessing elements
print("First coordinate:", coordinates[0])

# Tuple unpacking
x, y = coordinates
print("Unpacked x:", x, "Unpacked y:", y)

# 3. DICTIONARIES: Key-value pairs, mutable
print("\n=== Dictionaries ===")
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
print("Student Dictionary:", student)

# Modifying dictionary
student["age"] = 22  # Updating a value
student["GPA"] = 3.8  # Adding a new key-value pair
print("Updated Student:", student)

# 4. SETS: Unordered, unique collections
print("\n=== Sets ===")
unique_numbers = {1, 2, 3, 4, 4, 5}  # Duplicates are removed automatically
print("Unique Numbers Set:", unique_numbers)

# Practical Application: Data Structures in a Construction Company
print("\n=== Practical Application in Construction ===")

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
# budget=0;
# for item in materials:
#     if item == "cement":
#         budget += materials[item]*price_per_unit[item]
#     elif item == "sand":
#         budget += materials[item] * price_per_unit[item]
#     elif item == "bricks":
#         budget += materials[item] * price_per_unit[item]
#     elif item == "steel rods":
#         budget += materials[item] * price_per_unit[item]
#     else:
#         print("Budget is {item}")
# print("Total Budget Cost:", budget)
# Using the reusable function
total_cost = calculate_material_cost(materials, price_per_unit)
print("Total Material Cost:", total_cost)

# # Listing active machinery using a list
# machinery = ["Excavator", "Bulldozer", "Crane", "Mixer"]
# print("Active Machinery:", machinery)
#
# # Removing a machine under maintenance
# machinery.remove("Crane")
# print("After Removing Crane:", machinery)

goods = {
    "sugar": 500,  # bags
    "maggi": 1000,  # kg
    "water": 2000,  # pieces
}
print("Provision Store:", goods)

price_unit = {
    "sugar": 11,  # Price per bag
    "maggi": 13,  # Price per kg
    "water": 12,  # Price per piece
}
provision_cost = calculate_material_cost(goods, price_unit)
print("Store Inventory:", provision_cost)
# # Implementing recursion
# def newRecursion(k):
#     if k > 0:
#         result = k + newRecursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

#
# print("result from recursion function is:")
# newRecursion(6)

#

student_cgpa = {
    "umar": 3.5,
    "samuel": 4.1,
    "princess": 4.9,
}


# caluculate the sum of the gpa values
# calculate the length of students
# calculte the average only if the length is greater than 0
# return the calculated average.
def calculate_average_cgpa(student_cgpa):
    student_length = len(student_cgpa)
    cgpa_sum = sum(student_cgpa.values())
    # avg_cgpa = cgpa_sum / student_length if student_length > 0 else 0
    avg_cgpa2 = cgpa_sum // student_length if student_length > 0 else 0
    return avg_cgpa2


maut = calculate_average_cgpa(student_cgpa)
# print("average is :", round(maut, 2))
print("average option 2 is : ", maut)

# print("Average option 3 is : ", maut.__round__(2))
# print("Average option 4 is :" )
# print("Averge option 4 is :", maut.round())
