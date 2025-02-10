# Week 3
import math as m

my_dict = {}


def factorial_of_num(n):
    num_factorial = m.factorial(n)
    return print(num_factorial)


def multiply_dic():
    sums = 0
    sum_value=0
    j = 0
    for i in range(1, 16):
        if i%2 == 0 :
            sum_value += i
            j +=1
            print(i)
    #     sums += i
    #     my_dict[i] = i**2
    #     sum_the_square = my_dict[i] ** 2
    #     sum_value += my_dict[i]
    # print(f"the sum of the dictionary is {sums}")
    # print(f"the sum of the square is: {sum_the_square}")
    # print(f"the sum of the square is: {sum_value}")
    # print(f"the average of the values is: {sum_value/i}")
    print(f"the average of the even numbers is: {sum_value/j}")


factorial_of_num(9)