class1b = {}


def value_square():
    for i in range(1, 16):
        class1b[i] = i ** 2
    print(class1b)


def sum_dictionary():
    total_sum = sum(class1b.values())
    print(f'the total sum in the dictionary is:{total_sum} ')

def multiply_dictionary():
        multiplication = 1
        for i in class1b.values():
            multiplication *=i
        print(f'the multiplication of the values in the dictionary is:{multiplication} ')


value_square()
sum_dictionary()
multiply_dictionary()

