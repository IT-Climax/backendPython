#16Dec2024...
my_dict = {}
def sum_mult_of_dict():
    sums = 0
    sum_value = 0
    sum_of_even = 0
    j = 0
    for i in range(1,16):
        sums += i
        my_dict[i] = i**2
        sum_the_square = my_dict[i] ** 2
        sum_value += my_dict[i]
        # sum_of_even = i + 0
        if i%2== 0:
            sum_of_even += i
            j +=1
            print(i)
    print(f'The sum of the even numbers is: {sum_of_even}')
    print(f'The average of the even number is: {sum_of_even/7}')


def assignment_odd_avg():
    sum_of_odd = 0
    for i in range(1,16):
        x = 0
        x += 1
        if i % 2 != 0:
            sum_of_odd = i + sum_of_odd
            print(i)
    print(f'The sum of odd numbers is: {sum_of_odd}')
    print(f'The average of the odd numbers is: {sum_of_odd/8}')

#17Dec2024...
import math, random
def factorial():
    rand = random.randint(1,10)
    print(f'The factorial is: {math.factorial(8)}')
    print(f'Your remainder is: {math.fmod(20, 2)}')
    print(f'Your answer is: {math.fma(2,3,4)}')
    print(f'Your random number is: {random.randint(1,100)}')
    print(f'Your random number is: {rand}, and the factorial of your random number is: {math.factorial(rand)}')




# assignment_odd_avg()
# sum_mult_of_dict()
# factorial()