        # PRESENTATION
student_record = {}
def add_students():

    while True:
        name_of_student =input("\n Please enter the student's name: ").title()
        num_of_subject = int(input(f"  How many subjects does {name_of_student} takes?: "))

        for i in range(num_of_subject):
            subject = input(f"   Enter subject for {name_of_student}: ").title()
            scores = int(input(f"    Enter {name_of_student}'s {subject} score: "))

            if name_of_student not in student_record:
                student_record[name_of_student] = {}
            student_record[name_of_student][subject] = scores

        print(f" * {name_of_student} has been added successfully! * ")

        add_student = input("\nDo you want to add another student? (Y/N): ").lower()
        if add_student == 'y':
            continue
        elif add_student == 'n':
            break
        else:
            print("--------------------------")
            print("      Invalid option.")
            print("--------------------------")
            break


def view_record():
    if not student_record:
        print("    *Record is empty*\n *Press 1 to add student*")
    else:
        for name, subject in student_record.items():
            print(f" {name}:")
            for sub, score in subject.items():
                print(f"     {sub} - {score}")

        print("--------------------------")


def remove_student():
    if not student_record:
        print("\n    *Record is empty*\n *Press 1 to add student*")
    else:
        print("List of students:")
        for name, subject in student_record.items():
            print(f" {name}")
        name_to_remove = input("  Enter student name to remove from record: ").title()
        if name_to_remove in student_record:
            del student_record[name_to_remove]
            print(f"    {name_to_remove} has been removed successfully!")
        else:
            print("--------------------------")
            print(f"   Name not in records.")
            print("--------------------------")

def students_record():
    try:

        while True:
            print("\n***************************")
            print("     STUDENT'S RECORD")
            print("***************************")
            print(" 1. Add student")
            print(" 2. Remove student")
            print(" 3. View all students")
            print(" 4. Exit")
            print("***************************")

            option = int(input("Choose an option (1-4): "))


            if option == 1:
                add_students()
            elif option == 2:
                remove_student()
            elif option == 3:
                view_record()
            elif option == 4:
                print("               ...Exited")
                print("--------------------------")
                break
            else:
                print("    Invalid option.")
                print("--------------------------")

    except ValueError:
        print('      Error!!!\n Please entre a number.')


students_record()


