"""
Assignment for computation understanding of function definition
"""
import math


def factorial(n):
    """
    Compute the factorial of a number.

    Parameters:
        n (int): The number to compute the factorial of.

    Returns:
        int: The factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def gcd(a, b):
    """
    Compute the Greatest Common Divisor (GCD) of two numbers.

    Parameters:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: GCD of a and b.
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Compute the Least Common Multiple (LCM) of two numbers.

    Parameters:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: LCM of a and b.
    """
    return (a * b) // gcd(a, b)


def quadratic_roots(a, b, c):
    """
    Compute the roots of a quadratic equation ax^2 + bx + c = 0.

    Parameters:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        tuple: Two roots of the equation.
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "Complex Roots"
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2


def fibonacci(n):
    """
    Compute the nth Fibonacci number.

    Parameters:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    """
    if n <= 0:
        return "Invalid Input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def simple_interest(principal, rate, time):
    """
    Compute simple interest.

    Parameters:
        principal (float): The principal amount.
        rate (float): The annual interest rate in percentage.
        time (float): The time in years.

    Returns:
        float: The simple interest.
    """
    return (principal * rate * time) / 100


def compound_interest(principal, rate, time, n=1):
    """
    Compute compound interest.

    Parameters:
        principal (float): The principal amount.
        rate (float): The annual interest rate in percentage.
        time (float): The time in years.
        n (int): The number of times interest is compounded per year.

    Returns:
        float: The compound interest.
    """
    return principal * (1 + rate / (100 * n)) ** (n * time) - principal


def is_prime(n):
    """
    Check if a number is prime.

    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def arithmetic_sum(n, a, d):
    """
    Compute the sum of an arithmetic series.

    Parameters:
        n (int): Number of terms.
        a (int): First term.
        d (int): Common difference.

    Returns:
        int: The sum of the arithmetic series.
    """
    return (n / 2) * (2 * a + (n - 1) * d)


def pythagorean_theorem(a, b):
    """
    Compute the hypotenuse using the Pythagorean theorem.

    Parameters:
        a (float): Length of one leg.
        b (float): Length of the other leg.

    Returns:
        float: The length of the hypotenuse.
    """
    return math.sqrt(a ** 2 + b ** 2)


def matrix_multiplication(A, B):
    """
    Multiply two 2x2 matrices.

    Parameters:
        A (list of lists): First 2x2 matrix.
        B (list of lists): Second 2x2 matrix.

    Returns:
        list of lists: Resultant 2x2 matrix after multiplication.
    """
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]


# Example usage
factorialExample = factorial(6)
print("Factorial of 5:", factorialExample)
print("GCD of 24 and 36:", gcd(24, 36))
print("LCM of 4 and 6:", lcm(4, 6))
print("Quadratic roots of x^2 - 5x + 6:", quadratic_roots(1, -5, 6))
print("10th Fibonacci number:", fibonacci(10))
print("Simple Interest (P=1000, R=5, T=2):", simple_interest(1000, 5, 2))
print("Compound Interest (P=1000, R=5, T=2, N=2):", compound_interest(1000, 5, 2, 2))
print("Is 29 prime?", is_prime(29))
print("Sum of first 5 terms in A.P (a=2, d=3):", arithmetic_sum(5, 2, 3))
print("Hypotenuse of triangle with sides 3 and 4:", pythagorean_theorem(3, 4))

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("Matrix multiplication result:", matrix_multiplication(A, B))
