# Week 2 class 2

class3b = {"Name": "Grade"}
names = ['Ada', 'John', 'Love', 'Peter', 'Grace', 'Glory']


def add_student_and_grade():
    for name in names:
        grade = int(input(f'enter {name} grade: '))
        class3b[name] = grade

    print(class3b)


def add_generic_no_student():
    n = int(input("how many students do you have in your class? "))
    for i in range(n):
        name = input("The student's name is: ")
        grade = int(input(f'enter {name} grade: '))
        class3b[name] = grade
    print(class3b)


def retrieve_student_grade():
    name = input("please enter the students name: ")
    grade = class3b[name]
    print(f'{name} got {grade} marks')


# add_student_and_grade()
add_generic_no_student()

retrieve_student_grade()