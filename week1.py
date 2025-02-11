def introduction():
    name = (input('What is your name?: '))
    birth_year = int(input("Entre your birth year: " ))
    age = 2024 - birth_year
    year_to_100 = birth_year + 100
    print(f'Hello {name}... ')
    print(f"You are {age} years old. ")
    print(f"You will be 100 years old in {year_to_100}")


def multiplication_table():
    num = int(input('Entre the number: '))
    for x in range(1,13):
        multi = num * x
        print(f'{num} * {x} = {multi}')


def fact():
    num = int(input('Entre number to calculate its factorial: '))
    factorial = num
    if num == 0:
        print('The factorial of 0 is 1')
    elif num < 0:
        print ("Undefined")
    else:
       for i in range(1,num):
           factorial *=   i
       print(f'The factorial of {num} is {factorial}')


# num = 4
# for i in range(1, num):
#     num*=i
# print(num)

def factors_of_4():
    num = int(input('Entre any number: '))
    for i in range(num,50 + 1):
        if i % num == 0:
            print(f'{i} is a factor of {num}')


def average():
    stud = {'jo': [10,15,20,25,10], 'st':[12,23,15,7,20], 'ez':[10,10,10,10,5]}
    name = input('enter a name to see scores and average: ')
    print(f"This is {name}'s scores: {stud[name]}")
    avg_jo =  (10+15+20+25+10)/5
    avg_st = (12+23+15+7+20)/5
    avg_ez = (10+10+10+10+5)/5
    if name == 'jo':
        print(f"and jo's average is: {avg_jo}")
    elif name == 'st':
        print(f"and st's average is: {avg_st}")
    else:
        print(f"and ez's average is: {avg_ez}")

# print(stud[name])







#introduction()
#multiplication_table()
# fact()
#factors_of_4()
# average()