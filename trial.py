#
#
#
#
import random
def login():
    sign_up_name = input('Create username: ')
    sign_up_password = input('Create password: ')
    rand = random.randint(1, 10000)
    print('Account created successfully!')
    check = input('Do you want to log in to your account? Yes/No: ')
    if check.lower() == 'yes':
        name = input('Enter your username: \n')
        password = input('Enter your password: \n')

        if name == sign_up_name and password == sign_up_password:
            print(f'Code: {rand}')
            code = int(input('Enter the code displayed: '))
            if code == rand:
                print('Login successful!')
            else:
                print("Invalid code.")
        else:
            print('Invalid login details!')
    else:
        print('Thank you for creating an account with us.')

# login()
#
#
# def play_game():
#     username = input('Enter your name to begin game: ')
#     while True:
#         print(f'Welcome, {username}, to THE FOREST OF THE LOST.')
#         print("You are in a dark forest. "
#               "To your 'left', you see a dimly lit path. "
#               "To your 'right', you hear the sound of a rushing river. ")
#         choice1 = input("Do you go 'Left' or 'Right'?: ")
#         if choice1.lower() == 'left':
#             print('At the end of the dimly lit path you encounter a strange person')
#             choice2 = input("Do you 'Talk' to the stranger or 'Run' away: ")
#             if choice2.lower() == 'talk':
#                 print("The stranger leads you out of the dark forest. ")
#                 print(f'Congratulations {username}, you win!!!.')
#             elif choice2.lower() == 'run':
#                 print("You run away and forever get lost in the dark forest.")
#                 print("Game over!!!")
#
#                 while True:
#                     restart1 = (input('Do you want to start over?(y/n): '))
#                     if restart1.lower() == 'y':
#                         continue
#                     elif restart1.lower() == 'n':
#                         print('Terminated')
#                         break
#                     else:
#                         print('Invalid option')
#                         continue
#                 break
#             else:
#                 print('Invalid choice. Game over!!!')
#
#         elif choice1.lower() == 'right':
#             print("You try to cross the river but you get swept away by the current.")
#             print('Game over!!!')
#
#             restart2 = (input('Do you want to start over?(y/n): '))
#             if restart2.lower() == 'y':
#                 continue
#             elif restart2.lower() == 'n':
#                 break
#             else:
#                 print('Invalid option')
#             print('Terminated')
#         else:
#             print('Invalid choice. Game over!!!')
# # play_game()
#
#
# balance = 0
# def deposit():
#     amount = float(input("Enter the amount to be deposited: N"))
#     if amount <= 0:
#         print("Enter a amount greater than N0.00")
#         return 1
#     else:
#         print(f'N{amount:.2f} has been deposited successfully!')
#         return amount
#
# def withdrawal():
#     withdraw = int(input("Enter amount to be withdrawn: N"))
#     if withdraw > balance:
#         print("Insufficient funds")
#         return 0
#     elif withdraw <= 0:
#         print("Amount must be greater than N0.00")
#         return 0
#     else:
#         print(f'N{withdraw:.2f} has been withdrawn successfully!')
#         return withdraw
#
# def check_balance():
#     print(f"Your balance is N{balance:.2f}")
#
# while True:
#     print("Welcome to Pinnacle Bank")
#     print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
#
#     choice = int(input("choose an option to continue(1-4): "))
#     if choice == 1:
#         balance += deposit()
#     elif choice == 2:
#         balance -= withdrawal()
#     elif choice == 3:
#         check_balance()
#     elif choice == 4:
#         break
#     else:
#         print("Invalid choice.")
#
#
# deposit()
# withdrawal()
#
#
#
#
#
#
#
#
# def trying():
#     students = {'John': ['Math;41', 'English;72', 'Computer;86', 'Science;54', 'Art;60'],
#                 'Joe': ['Math;75', 'English;89', 'Computer;76', 'Science;79', 'Art;57'],
#                 'Ali': ['Math;77', 'English;30', 'Computer;58', 'Science;45', 'Art;63'],
#                 'Ben': ['Math;67', 'English;73', 'Computer;48', 'Science;51', 'Art;77']}
#     print(students)
#
# import random
#
# code = random.randint(1,10000)
# print(code)
# enter = int(input('Enter the random number displayed: '))
# if code == enter:
#     print('correct value')
# else:
#     print('Incorrect value')
# record=[]
#
#
# def add_student():
#     print('\nStudent Management Records\n1. Add student\n2. View students\n3. Remove student\n4. Exit')
#     options = int(input('Pick a number: '))
#     if options == '1':
#         name = input('enter student name: ')
#         age = int(input("enter student's age: "))
#         gender = (input('Gender(M/F): ')).lower()
#         student.append({'Name': name, 'Age': age, 'Gender': gender})
#         print(f'{name} has been added successfully')
#         print(f'List of students:\n{student}')
#     elif options == '2':
#         pass
#     elif options == '3':
#         pass
#     elif options == '4':
#         pass
#     else:
#         print('Invalid option, please try again.')
#
#
# student = []
# def add():
#     records = {
#         'name': input("enter name to add student to record: "),
#         'age': int(input("enter age of student: ")),
#         'gender': input("enter gender of student(M/F): ").lower()
#     }
#     if records['gender'] != 'm' or 'f':
#         print('Invalid gender')
#     else:
#         print(f"{records['name']} has been added successfully!")
#
#     def view():
#         student.append(records)
#         print(student)
#
#     return view
# valid = add()
#
#
# def exiting():
#     pass
#
#
# while True:
#     print('\nStudent Management Records\n1. Add student\n2. View students\n3. Remove student\n4. Exit')
#     choice = input('choose an option(1-4): ')
#     if choice == '1':
#         add()
#     elif choice == '2':
#         valid()
#     elif choice == '4':
#         break
#     else:
#         print('Invalid option.')
# print('EXITED')
#
#
# new = []
# def data():
#         option = input("1: Add a new student\n"
#                         "2: Remove an existing student\n"
#                         "3: Exit\n"
#                         "Choose an option: ")
#         while True:
#             if option == '1':
#                 info = {
#                     'name': input('enter student name: \n'),
#                     'age': int(input('Enter students age: \n')),
#                     'class': input('enter student class: \n')
#                 }
#                 new.append({'inf': info})
#                 check = input('Do you want to add another student or view student info?(yes/no/view): ')
#                 if check.lower() == 'yes':
#                     continue
#                 else:
#                     break
#             elif option == '3':
#                 print('Terminated!')
#                 break
# data()
#
# names = ['Abigail', 'Musa', 'Sarah', 'David', 'Ali']
# subjects = ['math', 'english', 'computer', 'economics']
# grades = [74, 44, 96, 61, 67]
# details = {
#     'name': ['Abigail', 'Musa', 'Sarah', 'David', 'Ali'
#                                                   'subject']
# }
#
# def student_management():
#     while True:
#         command = input("1: Add a new student\n"
#                         "2: Remove an existing student\n"
#                         "3: View all students\n"
#                         "4: Exit\n"
#                         "Choose an option: ")
#         if command == '1':
#             add = input("type name of student")
#             print(add)
#
#
# student_management()
#

def trying():
    user1  = ["001", '002']
    user1pass = ['0010', '0020']
    user_names = ['Joe', 'Dave']



    users = input("enter card number: ")
    passwords = input("enter password number: ")

    if users == user1[0] and passwords == user1pass[0]:
        print(f"welcome {user_names[0]}")
    elif users == user1[1] and passwords == user1pass[1]:
        print(f"welcome {user_names[1]}")
    else:
        print("user not found")
# trying()

def addition():
    total_sum = 0
    num1 = int(input("enter a number: "))
    num2 = int(input("enter another number: "))
    result = num1 + num2
    total_sum = result+total_sum
    print(f"{num1} + {num2} = {result}")
    while True:
        ask = input("Do you want to add another number? (y/n): ").lower()
        if ask == "y":
            num3 = int(input("enter the number: "))
        elif ask == "n":
            print(f"{total_sum + num3}")
            break


# addition()

def sum():
    total = 0
    while True:
        num1 = int(input("enter a number: "))
        number = num1
        total += number
        break
    print(total)

# sum()
def something():
    dict = {"name": "joe", "class": "ss1", "school": "high school"}
    for i, j in dict.items():
        print(f"{i}: {j}")

# something()


names = ['joe', 'jim', 'john']
scores = ['78', '86', '54']
with open('texts.txt', 'w') as op:
    for i in range(0, 3):
        details = names[i] + '-' + scores[i]+'\n'
        op.write(details)


StudentsRecords = []
StudentsRecords1 = []
StudentsRecords2 = []
def remove_something():
    with open('texts.txt', 'r') as of:
        for line in of.readlines():
            StudentsRecords.append(line)
        print(f'{StudentsRecords}')

    print("")

    for items in StudentsRecords:
        new = items.replace("\n","")
        StudentsRecords1.append(new)
    print(StudentsRecords1)

    name = str(input("entre name to remove: "))
    for items in StudentsRecords1:
        new = items.replace(name, "")
        StudentsRecords2.append(new)
    print(StudentsRecords2)


with open('texts.txt', 'w') as of:
    for i in StudentsRecords2:
        of.write(i)



remove_something()