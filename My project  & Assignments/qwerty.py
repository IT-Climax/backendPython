import math


def odd_addition():
    sum=0
    j=0


    for num in range(1,1000):
        if num % 3 == 0:
            j+=1
            sum+=num

    average=sum/j


    print(average)
    print(j)
odd_addition()


import math as m

def factorial_number():

    factorial=m.factorial(5)

    print(factorial)

factorial_number()

import random
def random_number():
    p=random.randint(1, 100)
    print(p)
random_number()


def rand_fact():
    import math
    import random
    calc = random.randint(1, 10)
    print(calc
