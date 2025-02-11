from os import name


# list this is a list
def players():
    football = ["Halland", "Messi", "CR7", "Neymar", "fabrigas", "osimen"]
    # to add aditional person to the list you append ----football.append("lookman")
    # to remove a person from the list you remove---- football.remove('the name you want to remove')
    # to modify (to change,replace) you type ----football[the number of what you want to replace] = "the name you want to input"
    # to calculate the length or the number of list you type -------print(len(football))
    print(football)
    football.append("Isaac")
    print(football)
    football.remove("Isaac")
    print(football)
    print(football[0])
    football[1] = "stephen"
    print(football)
    print(len(football))
    for player in football:
        if player == "CR7":
            print(f"i am the greatest player of all time")
        else:
            print(f"i am{player} the great player")


# dictionary this is a dictionary
def students_grades():
    names = {'Adam': 60, 'Ayuba': 100, 'Matthew': 80, }
    for a, b in names.items():
        print(a, b)
        pass
    try:
        average = input("do you want to get average (y/n): ".title())
        if average == "y":
            print(sum(names.values()) / 3)
        elif average == "n":
            print("thanks ")
    except TypeError:
        print("pls try again")


class3b = {"Names": "Grade"}
names = ['Ada', 'John', 'Love', 'Peter', ]


def add_student_and_grade():
    try:
        for name in names:
            grade = int(input(f'enter {name} grade: '))
            class3b[name] = grade
            print(class3b)
    except ValueError:
        print("check your input")




def add_generic_no_student():
    n = int(input("how many students do you have in your class? "))
    for i in range(n):
        name = input("the students name is: ")
        grade = int(input(f'enter{name} grade: '))
        class3b[name] = grade
    print(class3b)



def collect_name_department():
    try:
        n = int(input("please input the number of people you have in your department. "))
        for i in range(n):
            strings = input("the name of the worker: ")
            department = input("the name of the department: ")
            class3b[strings] = department
            print(class3b)
    except ValueError:
        print("check your input out. ")
def retrieve_department():
    try:
        name = input("enter the name you want to retrieve. ")
        print(f'{name} is in {class3b[name]} department.')
    except KeyError:
        print("check your spellings out. ")






# players()
# students_grades()
add_student_and_grade()
# add_generic_no_student()
#collect_name_department()
#retrieve_department()
