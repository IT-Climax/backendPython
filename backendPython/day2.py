# def error_solve():
#     try:
#         num = input("enter a number: ")
#         print(10 / num)
#     except TypeError:
#         print("this is a string")
#
#
# def class_work():
#     try:
#         num = int(input("enter a number here"))
#         print(num)
#     except ValueError:
#         print("kindly enter a number")
#
#
# def class_work2():
#     try:
#         num = int(input("enter your first number: "))
#         form = int(input("input your second number: "))
#         x = num + form
#         print(f"{x}")
#     except ValueError:
#         print("input a number")
#
#
# def multi_table():
#     try:
#         mul = int(input("input your desired number  "))
#         for i in range(13):
#             x = mul * i
#             print(f'{mul} * {i} = {x}')
#
#     except ValueError:
#         print("input a number not string. ")
#
#
# def year_calc():
#     try:
#         name = str(input("please insert your name: "))
#         age = int(input("please insert your age: "))
#         year = 2024 + (100 - age)
#         print(f'your name is {name}, you are {age} years old and you will be 100 years in {year}')
#     except ValueError:
#         print("Input a number not a name as your age. ")
#
#
# def fact_calc():
#     try:
#         num = int(input("input your factor: "))
#         factorial = num
#         if num == 0:
#             print("i am 0")
#         elif num < 0:
#             print("i am a negative number")
#         else:
#             for i in range(1, num):
#                 factorial = factorial * i
#                 print(f"the factorial of {num} is {factorial}")
#     except ValueError:
#         print("input a number not a word")




print(2//2)
# error_solve()
# class_work()
# class_work2()
# multi_table()
#year_calc()
# fact_calc()
