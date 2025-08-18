# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    name = input("please enter your name: ")
    birth_year = int(input("enter your birth year: "))
    age = 2024 - birth_year

    print(f"Hi, my name is, {name} and i am, {birth_year} years old and i was born in {age}")  # Press Ctrl+F8 to toggle the breakpoint.


def Area_calc():
    length = int(input("the length of a rectangle: "))
    breath = int(input("the breath of a rectangle: "))
    area = length * breath
    print(f'the area of the rectangle is {area}')


def perimeter_calc():
    length = int(input("please enter the length of your square: "))
    bred = int(input("please enter the breath of your square: "))
    perimeter = 2 * length + bred
    print(f'the perimeter of a square is {perimeter}')


def year_calc():
    name = input("please insert your name: ")
    age = int(input("please insert your age: "))
    year = 2024 + (100 - age)
    print(f'your name is {name}, you are {age} years old and you will be 100 years in {year}')


def if_statement():
    shape_name = input("what shape do you have:")
    if shape_name == "circle":
        radius = int(input("what is the radius of your circle: "))
        area = 3.14 * radius ** 2
        print(f'the area of your circle is {area}')
    elif shape_name == "triangle":
        base = int(input("what is the length of the base of your triangle?  "))
        height = int(input("what is the height of your triangle  "))
        area = (base / 2) * height
        print(f'the area of your triangle is {area}')
    else:
        print("the shape is not a triangle or circle")
        length = int(input("enter the length"))
        breath = int(input("enter the breath, if you have a square enter the length again  "))
        area = length * breath
        print(f'the area of the square is {area}')


def while_loop():
    count = 0
    while count < 5:
        print(count)
        count += 1
        print(count)
    for i in range(1, 6, 2):
        # in the i range 1 is the startin poin 6 is the ending point while 2 is the amount of time it will jump
        print(f'i am printing {i} time(s)')


def positive_calc():
    number = int(input("input your number"))
    if number > 0:
        print("i am a positive number")
    elif number == 0:
        print("i am a positive number ")
    else:
        print("i am a negative number ")


def multi_table():
    mul = int(input("input your desired number  "))

    for i in range(1, 13):
        x = mul * i
        print(f'{mul} * {i} = {x}')


def test_me():
    score = int(input("please input your score: "))
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("you failed your exams")


def fact_calc():
    num = int(input("input your factor: "))
    factorial = num
    if num == 0:
        print("i am 0")
    elif num < 0:
        print("i am a negative number")
    else:
        for i in range(1, num):
            factorial = factorial * i
        print(f"the factorial of {num} is {factorial}")


# for factorial num is the number


def modulo_calc():
    mod = int(input("input the number you want to calculate its modulo: "))
    modulo = mod
    for i in range(1, 100):
        fix = mod % 4
    print(f'the modulo of {modulo} is = {fix}')


def factor_of_four():
    first = int(input("input the upper bound: "))
    second = int(input("the lower bound: "))
    


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # Area_calc()
    # perimeter_calc()
    # year_calc()
    # if_statement()
    # while_loop()
    # positive_calc()
    # multi_table()
    # test_me()
    fact_calc()
    # modulo_calc()
