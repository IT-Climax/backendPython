def practice_1():
    name = int(input("please input you age:  "))
    if name >= 21:
        print("you are a adult")
    elif name <= 20:
        print("you are a teenager")
    elif name <= 12:
        print("you are an baby")
    else:
        print("you are out of the team")


def practice_2():
    mul = int(input("what number will you like to multiply? "))
    for i in range (1,13):
        num= mul*i
        print(f'{mul} * {i} = {num}')



def area_calc():
    try:
        name = input("input the shape you want to calculate its area: ")
        if name == "square":
            len = int(input("input the length of th square: "))
            bred = int(input(" the breath of the square: "))
            area = len * bred
            print(f"the area of a square is {area}")
        elif name == "triangle":
            hight = int(input("input the length of th triangle: "))
            base = int(input(" the breath of the Triangle: "))
            area = hight * base / 2
            print(f'{area}')
        else:
            print("the lord is your strength")
    except ValueError:
        print("check your input ")


def mul_tab():
    name = int(input("write the number you wnt to multiply: "))
    for i in range (1, 13):
        mul = i * name
        print(f'{name} * {i} = {mul}')


dictionary = {}


def dict_squar():
    for i in range (1, 21):
        dictionary[i] = i ** 2
    print(f'{dictionary}')


def summing():
    total= sum(dictionary.values())
    print(f'{total}')

def multiply():
    mul = 1
    for i in (dictionary.values()):
        mul *= i
    print(f'{mul}')



# #practice_1()
# #practice_2()
# #area_calc()
# #mul_tab()
# dict_squar()
# summing()
multiply()