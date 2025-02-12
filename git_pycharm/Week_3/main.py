"""squares_dict = {}
for x in range(1, 16):
        squares_dict[x] = x**2

print(squares_dict)
print(for {**2} )
"""

def multiply_dic():
    sums = 0
    sum_value = 0
    my_dict = {}
    for i in range(1, 16):
        j = 0
        sums += i
        my_dict[i] = i ** 2
        sum_value += my_dict[i]


#        if j % 2 == 0:


        print(f"The sum of the keys is: {sums}")
        print(f"The sum of the squares is: {sum_value}")
        print(f"The average of the squared values is: {sum_value / len(my_dict)}")
        print(f"The dictionary is: {my_dict}")

multiply_dic()


"""def sum_dict_items(input_dict):

    total_sum = 0

    for key, value in input_dict.items():
        total_sum += key + value

    return total_sum
example_dict = {
    2: 3,
    4: 5,
    6: 7,
}
result = sum_dict_items(example_dict)
print(f"The sum of all keys and values in the dictionary is: {result}")
"""