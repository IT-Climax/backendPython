
# What are Python Libraries?
# Pre-written modules that add functionality to Python.
#
# Examples: math, random, os.
#
# Importing Libraries
#
# Import the entire library:

import math
print(math.sqrt(16))

# Import specific functions:

from math import sqrt
print(sqrt(16))

# Use aliases for convenience:

import math as m
print(m.sqrt(16))

# Common Built-in Libraries
# Mathematical operations

math.sqrt(25)

# random

# Generate random numbers

random.randint(1, 10)

# os
# Interact with the operating system

os.listdir('.')

# Using External Libraries
# Install using pip:
# pip install numpy
# Example:

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr)

import math
def circle_area(radius):
    """Calculates the area of a circle given the radius."""
    return math.pi * math.pow(radius, 2)

# Call the function
print(circle_area(5))

# Write a function factorial(n) to calculate the factorial of a number.
# Use the random library to generate a random number between 1 and 100.
# Combine the two: Write a function to calculate the factorial of a random number.
