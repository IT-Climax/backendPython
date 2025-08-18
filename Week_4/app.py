# Handling division
try:
    num = float(input("Enter a number: "))
except ValueError:
    print("Enter a valid number.")


# Handling integer input errors
try:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    print(f"You entered {first_num} and {second_num}")
except ValueError:
    print("Enter a valid integer.")

# Repeating integer input handling
try:
    first_num = int(input("Please enter a valid number: "))
    second_num = int(input("Please enter a valid number: "))
    print(f"You entered {first_num} and {second_num}")
except ValueError:
    print("Enter a valid number.")