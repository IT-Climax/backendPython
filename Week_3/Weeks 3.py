def multiply_dic():
    sums = 0
    sum_value = 0
    my_dict = {}
        for i in range(1, 16):
           if i%2==0:

                i += 1
                print(i)
                sums += i
                my_dict[i] = i ** 2
                sum_value += my_dict[i]

        print(f"The dictionary is: {my_dict}")

multiply_dic()
