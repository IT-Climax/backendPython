
import math

# Program to pythagoras theorem

def pythagoras_theorem ():
    a = int (input(f"Enter A side: "))
    b = int (input(f"Enter B side: "))
    c_square = a**2 + b**2
    c = math.sqrt(c_square)
    print(f"answer is: {c:.2f}")


def factorial():
    number = int(input("Enter a number: "))
    facto = 1
    for fac in range (1, number + 1):
        facto *= fac
    print(f"The factorial of {number} is {facto}")

# Program to find the compound interest

def compound_interest():
    p = int(input("Enter principle: "))
    n = int(input("Enter number of compound period per year: "))
    r = float(input("Enter annual interest rate: "))
    y = int(input("Enter  the amount of years: "))
    compound_int = p * ((1+((r/100.0)/n))**(n*y))
    print(f"{compound_int:.2f}")


# pythagoras_theorem ()
factorial()
# compound_interest()