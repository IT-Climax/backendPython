


# Student Grades Function
def student_grade():
    name_of_the_student = {
        "moses": 80,
        "peter": 70,
        "john": 90,
    }
    for a, b in name_of_the_student.items():
        print(a, b)

    try:
        average = input("Do you want to calculate the average? (y/n): ").strip().lower()
        if average == "y":
            avg = sum(name_of_the_student.values()) / len(name_of_the_student)
            print(f"The class average is: {avg:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Dictionary for class grades
class3b = {}


def add_generic_no():
    n = int(input("How many students do you have in your class? "))
    for i in range(n):
        name = input("Please enter the student's name: ")
        try:
            grade = int(input(f"Enter {name}'s grade: "))
            class3b[name] = grade
        except ValueError:
            print("Invalid grade. Enter a number.")

    print("Class 3B Data:", class3b)


# Dictionary for employees
classC5 = {}


def employee_status():
    n = int(input("Enter the number of your employees: "))
    for i in range(n):
        name = input("Enter the employee's name: ")
        department = input(f"Enter {name}'s department: ")
        classC5[name] = department

    print("Employee Data:", classC5)


def retrieve_employee_dept():
    try:
        name = input("Please enter the employee's name: ").strip()
        department = classC5.get(name, "This name does not exist in the database.")
        print(f"{name} is in the {department} department.")
    except KeyError:
        print("An error occurred while retrieving data.")


# Calling the functions
add_generic_no()
#employee_status()
#retrieve_employee_dept()
