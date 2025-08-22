"""
Module 2: Data Structures in Python
------------------------------------
This script provides an in-depth understanding of Python data structures:
1. Lists
2. Tuples
3. Dictionaries
4. Sets
Each section includes explanations and examples.
"""

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
squared_numbers = [x**2 for x in range(5)]
print("Squared numbers:", squared_numbers)


# 2. TUPLES: Ordered, immutable collections
print("\n=== Tuples ===")
coordinates = (10.5, 20.3)  # Defining a tuple
print("Coordinates:", coordinates)

# Accessing elements
print("First coordinate:", coordinates[0])

# Tuples are immutable; modification is not allowed
# coordinates[0] = 15  # This would raise an error

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

# Accessing values
print("Student Name:", student["name"])

# Modifying dictionary
student["age"] = 22  # Updating a value
student["GPA"] = 3.8  # Adding a new key-value pair
print("Updated Student:", student)

# Looping through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")


# 4. SETS: Unordered, unique collections
print("\n=== Sets ===")
unique_numbers = {1, 2, 3, 4, 4, 5}  # Duplicates are removed automatically
print("Unique Numbers Set:", unique_numbers)

# Adding and removing elements
unique_numbers.add(6)
print("After adding 6:", unique_numbers)
unique_numbers.remove(3)
print("After removing 3:", unique_numbers)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a | set_b)  # Union of sets
print("Intersection:", set_a & set_b)  # Intersection of sets
print("Difference:", set_a - set_b)  # Difference of sets



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

# Updating inventory after usage
materials["cement"] -= 50  # Using 50 bags of cement
materials["bricks"] -= 500  # Using 500 bricks
print("Updated Inventory:", materials)

# Tracking project locations using tuples
project_sites = (
    ("Site A", "Downtown", 100),  # (Name, Location, Workers)
    ("Site B", "Uptown", 75),
    ("Site C", "Suburb", 50)
)
print("Project Sites:", project_sites)

# Keeping track of assigned engineers using sets
engineers = {"John", "Alice", "Robert", "Eve"}
print("Assigned Engineers:", engineers)
engineers.add("Michael")  # Adding a new engineer
print("After Adding Michael:", engineers)

# Listing active machinery using a list
machinery = ["Excavator", "Bulldozer", "Crane", "Mixer"]
print("Active Machinery:", machinery)

# Removing a machine under maintenance
machinery.remove("Crane")
print("After Removing Crane:", machinery)