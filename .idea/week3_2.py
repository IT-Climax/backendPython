# write a function to calculate the fact0orial of a number. use the in built pachage maths to do this
import math


def calculate_factorial(n):
    return math.factorial(n)


result = calculate_factorial(5)
print(result)
print(math.remainder(7, 9))

import random


def sel_rand(n,r):
    return random.randint(n,r)


result = sel_rand(1, 100)
print(result)
print(f'your random number is {random.randint(1, 100)}')
print(f" the factorial of a random number is {math.factorial(random.randint(1,100))}")
