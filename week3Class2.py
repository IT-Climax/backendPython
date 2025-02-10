# What are Functions?
#
# A function is a block of code designed to perform a specific task.
#
# Reusable, modular, and helps to avoid repetition.
#
# Creating a Function

# Define a function
def greet(name):
    """Greets a person by their name."""
    return f"Hello, {name}!"

# Call the function
print(greet("Alice"))

# Key Components of a Function
#
# Function Name: A unique identifier for the function (e.g., greet).
#
# Parameters: Optional variables passed to the function (e.g., name).
#
# Return Statement: Outputs a result (e.g., return f"Hello, {name}!").
#
# Why Use Functions?
#
# Reduces Redundancy: Write once, use multiple times.
#
# Improves Readability: Break code into logical units.
#
# Facilitates Debugging: Test individual components easily.
#
# Example: Reusable Function
# Function to calculate the square of a number

def calculate_square(number):
    """Returns the square of a number."""
    sums = number + number
    return "done"

# Using the function
result = calculate_square(5)
print(f"The square of 5 is {result}")