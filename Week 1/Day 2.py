from sys import excepthook

#try:
    #num = input("Enter a number: ")
   # print(10 / num)
#except TypeError:
   # print("integer cannot be divided by a string")

def classwork():
    try:
        number = int(input("kindly enter a number: "))
        print(number)
    except ValueError:
        print("kindly ensure you enter a number")


def second_classwork():
    try:
        number1 = int(input("enter first number: "))
        number_2 = int(input("enter second number: "))
        print(number1)
        print(number_2)
    except ValueError:
        print("Enter the numbers")

def multiplication_table_error_handling():
   try:
       multi = int(input("Enter Number to be Multiplied: "))
       for j in range(1, 13):
           multi_cal = multi * j
           print(f'{multi} * {j} = {multi_cal}')
   except ValueError:
       print("PLease Enter integer Number only to be multiplied")



def calculate_the_class_average(c_names):
    average = {}
    for c_names, grades in class_members.items():
        average[c_names] = sum(grades)/len(grades)
        print(f'{average}')
class_members = {'ismail': [60, 62, 76, 70], 'john': [50, 40, 71, 100], 'musa': [70, 45, 31, 88]}






#classwork()
#second_classwork()0.
#multiplication_table_error_handling()
calculate_the_class_average(c_names)




