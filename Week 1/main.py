# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    name = input("Please enter your name: ")
    print(type(name))
    birth_year = int(input("Please enter your birth year: "))
    print(type(birth_year))
    age = 2024 - birth_year
    print(age)
    print(f'Hi, {name}')

    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))

    area = length * breadth
    print (f' {area}')

def perimeter_cal():

    length = int(input("Enter Length: "))
    bred = int(input("Enter breadth: "))
    perimeter = 2 * (length + bred)
    print(f'perimeter is {perimeter}')



def age_cal():
    f_name = input("Enter your First Name: ")
    s_name = input("Enter your Surname: ")
    birth_year = int(input("Enter your Birth Year: "))
    age =  2024 - birth_year
    years_ahead = 100 - age
    years_ahead += 2024
    print(f' Hi, {f_name} {s_name}')
    print(f' Your {age} years old of age &')
    print(f' Your going to clock 100 years in {years_ahead}')


def if_statement():
    shape_name = input("what shape do you have: ")
    if shape_name == "circle":
        radius = int(input("what is the radius of your circle: "))
        area = 3.142 * radius ** 2
        print(f" the area of your circle is {area}")
    elif shape_name == "triangle":
        base = int(input("what is the base of your triangle?: "))
        height = int(input("what is length of the your triangle?: "))
        area = (base/2) * height
        print(f"the area of the triangle is {area}")
    else:
        print("the shape is not a triangle nor circle")
        length = int(input("enter the length: "))
        breadth = int(input("enter the breadth, if you have a square, enter the length again: "))
        area = length * breadth
        print(f"the area of your shape is {area}")

    print("i am outside the if")

def for_while_loop():
    count = 0
    while count < 5:
        print(count)
        count += 1
        print(count)
    for i in range(10):
        print(f" i am printing {i} time(s)")

def if_positive_negative():
    numbs = int(input("Enter positive or negative numbers: "))
    if numbs < 0:
        print(f' is a negative number')
    else:
        print(f'is a positive number')
        

def multiplication_table():
    multi = int(input("Enter the number: "))
    for i in range(1,13):
        multi_cal = multi * i
        print(f'{multi} * {i} = {multi_cal}')

def factorial_of_numbers():
    numb = int(input("Enter a Number to get it factorial: "))
    fact = 1
    for i in range(1, numb+1):
        fact *= i
        print(f' Factorial of {numb} is: {fact}')

def factorial_of_numbers_with_for_loop():
    try:
        numb = int(input("Enter a Number to get it factorial: "))
        fact = 1
        i = 1
        while i <= numb:
            fact *= i
            i += 1
            print(f' {fact}')
    except ValueError:
        print('An exception occurred')


#Press the green button in the gutter to run the script.


if __name__ == '__main__':


    #print_hi('PyCharm')

    #perimeter_cal()
    #age_cal()
    #if_statement()
    #for_while_loop()
    #if_positive_negative()
    #multiplication_table()
    #factorial_of_numbers()
    factorial_of_numbers_with_for_loop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
