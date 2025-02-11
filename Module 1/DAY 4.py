
class3b = {'name': 'grade: '}
names = ['ada', 'john', 'love', 'peter', 'grace', 'glory']


def add_student_and_grade():
    for name in names:
        grade = int(input(f'Enter {name} grade: '))
        class3b[name] = grade

    print(class3b)


def add_generic_no_student():
    n = int(input("how many students do you have in your class?  "))
    for i in range(n):
        names = input("The student is: ")
        grade = int(input(f'Enter {names} grade: '))
        class3b[names] = grade
    print(class3b)



details = {'names: ' 'department: '}
employees = ['ismail', 'musa', 'john', 'merry']

def employee_details():
    n = int(input("how many employee are there in your department?  "))
    for i in range(n):
        names = input("The employee's Name is: ")
        department = input(f'Enter {names} department: ')
        details[names] = department
    print(details)

def retrieve_employee_details( ):
    names = input("please enter the employee's name: ")
    print(f'{names} is in the department of {details[names]}')

#Python Program to print the square of numbers 1 to 15 in a dictionary


def dictionary_of_numbers():
    print('The square of numbers 1-15 is as follows:')
    for items, values in numb_dic.items():
        print(f'{items} : {values}')



#Python Program to find the sum of all items in a dictionary

numb_dic = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100, 11:121, 12:144, 13:169, 14:196, 15:255}

def sum_of_numbers_in_dict():
    print(f'The sum of square in the dictionary is: {sum(numb_dic.values())}')

#Python Program to multiply all items in a dictionary

def multiply_dictionary_items():
    multiply = 1
    for values in numb_dic:
        multiply *= numb_dic[values]
    print(f'The multiplication of all the items in the dictionary is: {multiply}')

#Python Program to print a dictionary

def square_of_dictionary_items():
    square_dict = dict()
    for values in range(1, 16):
        square_dict[values] = values**2
    print(f'square_dict = {square_dict}')


my_dict = {}

def multiply_dict():
    sums = 0
    sum_value = 0
    for i in range(1, 16):
        sums += my_dict[i] **2
        sum_the_square = my_dict[i] **2
        sum_value += my_dict[i]
    print(f"the sum of the dictionary is {sums}")
    print(f"the sum of the square is: {sum_the_square}")
    print(f"the sum of the square is: {sum_value}")
    print(f"the average of the values is: {sum_value/i}")
    print(f"the dictionary is: {my_dict}")



def find_ave():
    sums = 0
    sum_value = 0
    j = 0
    for i in range(1, 16):
        if i%2 == 0:
            sum_value += i
            j +=1
            print(i)
    print(f"{sum_value/j}")



def average_of_even_numbs():
    
    for i in range(1, 16):
        if i%2 == 1:
            print(i)









#add_student_and_grade()
#add_generic_no_student()
employee_details()
#employees_profile()
#employee_details()
#retrieve_employee_details()
#dictionary_of_numbers()
#sum_of_numbers_in_dict()
#multiply_dictionary_items()
#square_of_dictionary_items()
#multiply_dict()
#find_ave()
#average_of_even_numbs()
