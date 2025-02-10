# This is a sample Python script.
# Week 1 classes 2 and 3
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    name = input("Please enter your name: ")
    birth_year = int(input("Please enter your birth year: "))
    age = 2024 - birth_year
    print("Hi my name")
    print(f'Hi, my name is, {name}, and I am, {age} year old')  # Press Ctrl+F8 to toggle the breakpoint.


def perimeter_calc():
    len = int(input("Enter the length: "))
    breadth = int(input("Enter the breadth: "))
    peri = 2*(len + breadth)
    print(f'The perimeter is: {peri}')


def area_calc():
    len = int(input("Please enter the length of your rectangle: "))
    bred = int(input("please enter the breadth of your rectangle: "))
    area = len * bred
    print(f'The area of the rectangle is {area}')


def if_statement():
    shape_name = input("What shape do you have: ")
    if shape_name == "circle":
        radius = int(input("what is the radius of your circle: "))
        area = 3.14 * radius ** 2
        print(f"The area of your circle is {area}")
    elif shape_name == 'triangle':
        base = int(input('What is the length of the base of your triangle? '))
        height = int(input('what is the height of your triangle '))
        area = (base/2) * height
        print(f'The area of the triangle is {area}')
    elif shape_name == 'trapezium':
        a = int(input('Enter a: '))
        b = int(input("Enter b: "))
        height = int(input('what is the height of your triangle '))
        area = 0.5*(a+b) * height
        print(f'The area of the trapezium is {area}')
    else:
        print('the shape is not a triangle nor circle')
        length = int(input("enter the length: "))
        breadth = int(input("enter the breadth, if you have a square, enter the lenght again "))
        area = length * breadth
        print(f'The area of your shape is {area}')

    print('I am outside the if')


def for_while_loop():
    count = 0
    while count < 5:
        print(count)
        count += 2
        print(count)
    for i in range(1, 6, 3):
        print(f'i am printing {i} time(s)')


def positive_or_negative():
    x = int(input("Enter any number: "))

    if x < 0:
        print(f'{x} is a negative number')
    elif x > 0:
        print(f'{x} is a positive number')
    else:
        print('I am zero')


def n_multiplication_table():
    n = int(input("Enter the number you want its multiplication table "))

    for i in range(13):
        multiple = i * n
        print(f'{i} * {n} = {multiple}')


def factorial_calc():
    n = int(input("Enter a positive number"))
    for i in range(1, n):
        n *= i
    print(n)


def factor_of_four():
    beginning = int(input("Please enter the lower bound: "))
    end = int(input("please input the upper bound: "))
    print('the factors of 4 are: ')
    try:
        for i in range(beginning, end):
            print("i am a print statement")
            if i % 4 == 0:
                print("I am working")
                b = "backend"
                a = i/0
                print(a)
    except TypeError:
        print("Enter a number and  not a string")
    except ZeroDivisionError:
        print("Will you STOP!!! you cant divide by 0")


# Press the green button in the gutter to run the script. ctrl+/
if __name__ == '__main__':

    # perimeter_calc()
    # print_hi('PyCharm')
    # area_calc()
    # if_statement()
    # for_while_loop()
    # positive_or_negative()
    # n_multiplication_table()
    # factorial_calc()
    factor_of_four()
