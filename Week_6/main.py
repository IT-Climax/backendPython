materials = {
    'concrete': 500,
    'sand': 1000,
    'bricks': 2000,
    'steel rods': 150
}

per_unit = {
    'concrete': 10,
    'sand': 5,
    'bricks': 2,
    'steel rods': 15
}



def cost_of_materials():
    total_cost = 0
    for key in materials:
        if key == 'concrete':
           total_cost += materials[key] * per_unit[key]
        elif key == 'sand':
            total_cost += materials[key] * per_unit[key]
        elif key == 'bricks':
            total_cost += materials[key] * per_unit[key]
        elif key == 'steel rods':
            total_cost += materials[key] * per_unit[key]
        else:
            print('invalid')
    print(f'Total cost of materials = ₦{total_cost}')

# cost_of_materials()

students = {
        'student1': 4.1,
        'student2': 3.5,
        'student3': 2.7,
        'student4': 4.5,
        'student5': 3.8,
        'student6': 2.9,
        'student7': 4.4,
        'student8': 5.0,
        'student9': 4.3,
        'student10:': 3.7,
        'student11': 4.0,
        'student12': 4.2,
        'student13': 3.6,
        'student14': 4.8,
        'student15': 3.3,
        'student16': 3.5,
        'student17': 2.1,
        'student18': 4.1,
        'student19': 1.9,
        'student20': 2.6
    }


def average_cgpas(students):

    for key in students.items():
        cgpa_sum = sum(students.values())
        num_of_cgpa = len(students.values())
        if len(students.values()) > 0:
            cgpa_average = cgpa_sum/num_of_cgpa


    return cgpa_average


    # while True:
    #     cgpa_avg = sum(students.values()) / len(students.values())
    #     print(cgpa_avg.__round__(1))
    #     break

# avg = average_cgpas(students)
# print(' The average is', avg.__round__(2))





    # assignment1:1, compound interest.
    #             2, factorial. (5: 5*4*3*2*1)
    #             3, pythagoras theorem
    # assignment2:


'''        === ASSIGNMENT 1 ===         '''
P = 1000
r = 5
r = r/100
n = 12
t = 5
def calculate_compound_interest(P, r, n, t):
    # formula: A = p(1+r/n)^(nt)

    step1 = 1 + r/n
    step2 = n*t
    step3 = step1 ** step2

    A = P * step3 if P > 0 else 0

    print("\n  === Compound Interest ===")
    print('Compound Interest, A = p(1+r/n)^(nt)')
    print(f'    A = {P}({1 + r/n})^{step2}')
    print(f'    A = {P}({(1 + r / n)**60})')

    return A

compound_interest = calculate_compound_interest(P, r, n, t)
print('Compound Interest, A = ', compound_interest.__round__(2))
print('')


'''        === ASSIGNMENT 2 ===         '''
def calculate_factorial(n):
    try:
        print("      === Factorial ===")

        factorial = 1
        if n == 0:
            print('The factorial of 0 is 1')
        elif n < 0:
            print ("Number must be greater than 0")
        else:
           for i in range(1,n+1):
               factorial *= i
           print(f'The factorial of {n} is {factorial}')

    except ValueError:
        print('Error!!! Enter a number')
    except TypeError:
        print('ERROR!: Number must be an integer')

    return factorial

# calculate_factorial(5.9)
print('')

'''        === ASSIGNMENT 3 ===         '''
def calculate_pythagoras_theory(a,b,c):
    # formula:  c = √(a²+b²)
    #           b = √(c²-a²)
    #           a = √(c²-b²)

    print("=== Pythagoras' Theory ===")

    if c == 0:
        step1 = (a**2 + b**2)
        c = step1 ** 0.5
        print('To find c:   c = √(a²+b²)')
        print(f'    c = √({a**2} + {b**2}) ')
        print(f'    c = √({step1})')
        print(f'The value of c is: {c.__round__(2)}')
    elif b == 0:
        step1 = (c**2 - a**2)
        b = step1 ** 0.5
        print('To find b:   b = √(c²-a²)')
        print(f'    b = √({c ** 2} - {a ** 2}) ')
        print(f'    b = √({step1})')
        print(f'The value of b is: {b.__round__(2)}')
    elif a == 0:
        step1 = (c**2 - b**2)
        a = step1 ** 0.5
        print('To find a:   a = √(c²-b²)')
        print(f'    a = √({c ** 2} - {b ** 2}) ')
        print(f'    a = √({step1})')
        print(f'The value of b is: {a.__round__(2)}')
    else:
        print('      Invalid question')

    return c, b, a


# pythagoras_theory = calculate_pythagoras_theory(3,4,0)
#
# import sqlite3
# connection = sqlite3.connect("trial.db")
#
#
# connection.close()