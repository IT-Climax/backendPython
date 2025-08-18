"""
Module 2: Object-Oriented Programming in Python
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
"""

import math  # Example of importing a built-in Python library

# 1. Classes and Objects
print("\n=== Classes and Objects ===")

"""
A class is like a blueprint for creating objects. 
Imagine a house blueprint—it defines how the house should look, but you need to build an actual house from it.

Example: 
A Car class can define properties like color, model, and speed, but it doesn’t represent an actual car until you create one
"""


class ConstructionProject:
    """A class representing a construction project."""

    def __init__(self, name, location, budget, staff):
        self.name = name  # Attribute
        self.location = location  # Attribute
        self.budget = budget  # Attribute
        self.staff = staff

    def display_project_info(self):
        """Method to display project details."""
        print(f"Project: {self.name}, Location: {self.location}, Budget: ${self.budget}")

    def display_staff_info(self):
        "Method to display the staff name"
        print(f"Staff name:{self.staff}")

# Creating an object
"""
An object is an actual thing created from a class. 
If the class is the blueprint, the object is the house built from that blueprint.
Example: 
If Car is a class, then a red Toyota Corolla is an object of that class.
"""

project1 = ConstructionProject("Mall Construction", "Downtown", 500000)
staff1 = C
project1.display_project_info()
#
# # 2. Methods
# """
# A method is a function inside a class that defines what an object can do.
# Think of it as an ability or action.
# Example:
# A Car class may have a method called drive(), which makes the car move.
# """
#c
# print("\n=== Methods ===")
#
#
# class Machinery:
#     """A class to represent construction machinery."""
#
#     def __init__(self, name, status):
#         self.name = name
#         self.status = status
#
#     def update_status(self, new_status):
#         """Method to update machinery status."""
#         self.status = new_status
#         print(f"{self.name} is now {self.status}")
#
#
# excavator = Machinery("Excavator", "Operational")
# excavator.update_status("Under Maintenance")

# # 3. Inheritance
# """
# Inheritance allows a class to reuse properties and methods of another class,
# just like a child inherits traits from parents.
#
# Example:
# If there’s a Vehicle class, a Car class can inherit from it instead of rewriting everything.
# The Car class will automatically have the features of a Vehicle (like wheels and engine).
# """
# print("\n=== Inheritance ===")
#
#
# class Employee:
#     """Base class representing an employee."""
#
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
#     def work(self):
#         print(f"{self.name} is working as a {self.role}")
#
#
# class Engineer(Employee):
#     """Derived class representing an engineer, inheriting from Employee."""
#
#     def __init__(self, name, specialization):
#         super().__init__(name, "Engineer")
#         self.specialization = specialization
#
#     def design(self):
#         print(f"{self.name} is designing a {self.specialization} structure")
#
#
# engineer1 = Engineer("Alice", "Bridge")
# engineer1.work()
# engineer1.design()
#
# # 4. Encapsulation
# """
# Encapsulation is like hiding parts of an object to protect them from being changed accidentally.
# Think of it like your phone’s settings—only you can change them, not everyone.
# Example:
# A BankAccount class hides the balance so users can’t change it directly.
# They must use a deposit() or withdraw() method instead.
# """
# print("\n=== Encapsulation ===")
#
#
# class Budget:
#     """Class representing a project's budget."""
#
#     def __init__(self, amount):
#         self.__amount = amount  # Private variable
#
#     def get_budget(self):
#         """Getter method to access private variable."""
#         return self.__amount
#
#     def set_budget(self, new_amount):
#         """Setter method to modify private variable."""
#         if new_amount > 0:
#             self.__amount = new_amount
#         else:
#             print("Budget must be positive!")
#
#
# budget1 = Budget(1000000)
# print("Initial Budget:", budget1.get_budget())
# budget1.set_budget(1200000)
# print("Updated Budget:", budget1.get_budget())
#
# # 5. Polymorphism
# """
# Polymorphism means one thing can have multiple forms—just like how a
# trainee can be a student at at Mentors Hub and a sales person at a store.
# Example:
# A Bird class can have a fly() method, but different birds may fly differently.
# A Sparrow may fly fast, while a Penguin doesn’t fly at all but still has the fly() method (with different behavior).
# """
# print("\n=== Polymorphism ===")
#
#
# class Worker:
#     """Parent class representing a general worker."""
#
#     def perform_task(self):
#         print("Performing general construction tasks")
#
#
# class Electrician(Worker):
#     """Child class representing an electrician."""
#
#     def perform_task(self):
#         print("Installing electrical wiring and fixtures")
#
#
# class Plumber(Worker):
#     """Child class representing a plumber."""
#
#     def perform_task(self):
#         print("Fixing pipes and water systems")
#
#
# workers = [Electrician(), Plumber(), Worker()]
# for worker in workers:
#     worker.perform_task()
#
# # Practical Application: Construction Company Data Handling
# print("\n=== Practical Application in Construction ===")
#
# # Managing materials inventory using a dictionary
# materials = {
#     "cement": 500,  # bags
#     "sand": 1000,  # kg
#     "bricks": 2000,  # pieces
#     "steel rods": 150  # units
# }
# print("Construction Materials:", materials)
#
# price_per_unit = {
#     "cement": 10,  # Price per bag
#     "sand": 5,  # Price per kg
#     "bricks": 2,  # Price per piece
#     "steel rods": 15  # Price per unit
# }
#
#
# def calculate_material_cost(materials, price_per_unit):
#     """Reusable function to calculate material costs."""
#     total_cost = 0
#     for material, quantity in materials.items():
#         cost = quantity * price_per_unit.get(material, 0)
#         total_cost += cost
#         print(f"Cost for {material}: {cost}")
#     return total_cost
#
#
# # Using the reusable function
# total_cost = calculate_material_cost(materials, price_per_unit)
# print("Total Material Cost:", total_cost)
#
# # Listing active machinery using a list
# machinery = ["Excavator", "Bulldozer", "Crane", "Mixer"]
# print("Active Machinery:", machinery)
#
# # Removing a machine under maintenance
# machinery.remove("Crane")
# print("After Removing Crane:", machinery)
