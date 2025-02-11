import random
import math


def calculate_fact_rand(a, b):
    return random.randint(a, b)


result = calculate_fact_rand(1, 10)
print(result)
print(f"{math.factorial(result)} ")
