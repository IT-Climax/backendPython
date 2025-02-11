# try:
#     num = input('Entre a number: ')
#     print(10 / num )
# except TypeError:
#     print('entre a number not a string')
#from tkinter.font import names


#09Dec2024...
# def fact():
#     num = int(input('Enter a number:'))
#     cv = 1
#     for i in range(1, num+1):
#         cv *= i
#         print(cv)

# facts()
def mult_andrew():
    nums = 0

    while nums == 0:
        try:
            nums = int(input("Type the number: "))
            if nums in range(1, 14):
                for i in range(1, nums+3):
                    print(f"Your times table is {nums} * {i} = {nums * i}")
            else:
                raise ValueError
        except ValueError:
            nums = 0

            if nums == 0:
                print("Please your number should be between 1 - 13")
# mult_andrew()


def multiplication_table_error():
    try:
        num = int(input('Entre the number: '))
        for x in range(1,13):
            multi = num * x
            print(f'{num} * {x} = {multi}')
    except ValueError:
        print('Error!!!. Enter a number not a letter')

# multiplication_table_error()


def value_error():
    try:
        number = int(input('Enter a number: '))
        print(number)
    except ValueError:
        print('Error!!!. Enter a number not a string, retard!')


def value_error_ii():
    try:
        num_i = int(input('Entre a number: '))
        num_ii = int(input('Entre another number: '))
        print(f'{num_i} + {num_ii} = {num_i + num_ii}')
    except ValueError:
        print('Error!!!. Entre a number not a letter')


def factorial_error(n):
    try:
        # num = int(input('Entre number to calculate its factorial: '))
        factorial = 1
        if n == 0:
            print('The factorial of 0 is 1')
        elif n < 0:
            print ("Undefined")
        else:
           for i in range(1,n+1):
               factorial = factorial * i
           print(f'The factorial of {n} is {factorial}')
    except ValueError:
        print('Error!!! Enter a number')

    return factorial

factorial_error(0)



def factors_of_a_num():
    try:
        num = int(input('Entre any number: '))
        for i in range(num,50 + 1):
            if i % num == 0:
                print(f'{i} is a factor of {num}')
    except ValueError:
        print('Error!!! Enter a number!')


def introduction_error():
    try:
        name = (input('What is your name?: '))
        birth_year = int(input("Entre your birth year: " ))
        age = 2024 - birth_year
        year_to_100 = birth_year + 100
        print(f'Hello {name}... ')
        print(f"You are {age} years old. ")
        print(f"You will be 100 years old in {year_to_100}")
    except ValueError:
        print('Error!!! Enter a number!')

#10Dec2024...
def lists_tuples_dict_sets():
    subjects = ['Math', 'English', 'Physics', 'Chemistry', 'Biology', 'Literature']
    print(subjects)
    print(subjects[3]) #output = 'chemistry'
    subjects.append('F/Math')
    print(subjects) #output = subjects + 'F/maths'
    subjects.remove('Literature')
    print(subjects) #output = subjects - 'Literature'
    subjects[-1] = 'F/Math'
    print(len(subjects))
    for subject in subjects:
        print(subject)
    for subject in subjects:
        if subject == 'F/Math':
            print(f'I F/math, am the toughest!')
        else:
            print(f'{subject} is a tough subject')


def assignment_avg():
    try:
        students = {'John': ['Math;41', 'English;72','Computer;86', 'Science;54', 'Art;60'],
                    'Joe': ['Math;75','English;89','Computer;76','Science;79', 'Art;57'],
                    'Ali': ['Math;77','English;30','Computer;58','Science;45', 'Art;63'],
                    'Ben': ['Math;67','English;73','Computer;48','Science;51', 'Art;77']}
        name = input('Enter name of the Students: ')
        print(f"These are {name}'s scores: {students[name]}")
        avg_john = (41 + 72 + 86 + 54 + 60) / 5
        avg_joe = (75 + 89 + 76 + 79 + 57) / 5
        avg_ali = (77 + 30 + 58 + 45 + 63) / 5
        avg_ben = (67 + 73 + 48 + 51 + 77) / 5
        if name == 'John':
            print(f"and John's average is: {avg_john}")
        elif name == 'Joe':
            print(f"and Joe's average is: {avg_joe}")
        elif name == 'Ali':
            print(f"and Ali's average is: {avg_ali}")
        else:
            print(f"and Ben's average is: {avg_ben}")
    except KeyError:
        print('No student found with this name')


def assignment_set():
    box1 = {'apple', 'banana', 'grape', 'pear', 'mango'}
    box2 = {'mango', 'guava', 'apple', 'pineapple', 'banana'}
    print('we have these in common:')
    print(box1.intersection(box2)) #in common
    print('These are box1 unique items')
    print(box1.difference(box2))
    print('These are box2 unique items')
    print(box2.difference(box1))

# 11Dec2024...
class3a = {"Name": "Grade"}
# names = ['joe', 'musa', 'ali', 'grace', 'peter']
def classwork():
    n = int(input('How many students do you have?: '))
    for i in range(n):
        name = input('Enter students name: ')
        grade = int(input(f"Enter {name}'s grade"))
        class3a[name] = grade
    print(class3a)

# classwork()


def classwork2():
    n = int(input("how many student's do you have?: "))
    for i in range(n):
        name = input("student name is: ")
        grade = int(input())
# classwork()

info = {"Name":"Department:"}
def employee_data():
    try:
        n = int(input("Enter number of employees: "))
        for i in range(n):
            name = input("Enter employee name: ")
            dept = input("Enter employee department: ")
            info[name] = dept
        print(info)
    except ValueError:
        print('Error!!! Enter a number')
def retrieve():
    try:
        name = input('Enter name to retrieve department: ')
        print(f'{name} is in {info[name]} department')
    except KeyError:
        print('No employee found with this name! ')


def square_of_key():
     x=dict()
     for i in range(1,16):
         x[i]=i*i
     print(x)


def multiplication_of_values():
    scores={'math': 20, 'eng': 30, 'comp':40, 'art':50}
    mult=1
    for key in scores:
        mult=mult*scores[key]
    print(f'The product of scores is: {mult}')


def addition_of_values():
    scores = {'math': 20, 'eng': 30, 'comp': 40, 'art': 50}
    addition=sum(scores.values())
    print(f'The sum of the scores is: {addition}')







# square_of_key()
# employee_data()
# retrieve()
#value_error()
#value_error_ii()
#multiplication_table_error()

#factors_of_a_num()
#introduction_error()
#lists_tuples_dict_sets()
#assignment_avg()
#assignment_set()
# multiplication_of_values()
# addition_of_values()
