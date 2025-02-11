 bmy_dict ={}


def multiply_dict():
    sum = 0
    sum_value = 0
    for i in range (1, 16):
        sum += i
        my_dict[i] = i**2
        sum_the_square = my_dict[i] ** 2
        sum_value += my_dict[i]
        print(f' the sum of the dictionary is {sum}')
        print(f' the sum of the square is {sum_the_square}')
        print(f'the sum of the square is {sum_value}')
        print(f'the average of the value is: {sum_value / i}')
        print(f'the dictionary is: {my_dict}')



multiply_dict()