
# #espected to calculate the sum of all numbers from the range of 1,n
# def sum_calc(n):
#     n=int(input("input the number you want to sum"))
#     summing=0
#     for i in range (1,n):
#         summing += i
#         print(summing)
#
#
# def is_palindrome(s):
#     s=s.replace("",'').lower()
#     return s==s[::-1]
#
# # input_string = input('Enter a string:' )
# # if is_palindrome(input_string):
# #     print(f"{input_string} is a palindrome")
# # else:
# #     print(f"{input_string} is not a palindrome")
#
# # reverse a se of list without using reverse() method
# fruits =["mango","apple","orange", "pawpaw"]
# def reverse_string():
#     list= fruits[::-1]
#     print(list)
#
# #trying to find the largest number in a list
#
#
# numbers =[1,2,3,20,15,24,90,30,25,40]
# max = numbers[0]
# for x in numbers:
#         if x > max:
#             max = x
# print(f"{max}")


# at the end expected to show the minimum number
#
# min_numbers = [4,6,20,60,2,12,1,19,15]
# min = min_numbers[1]
# for s in min_numbers:
#     if s < min:
#         min = s
# print(f"{min}")

# hoping to show if it's a prime number or not (not correct)
def prime_number():
    num_prime = int(input("write the number you want to know if its a prime: "))
    if num_prime>1:
        for i in range(2, num_prime):
            if num_prime % i == 0:
                print(f'{num_prime} is not a prime')
                break
            else:
                print(f'{num_prime} is a prime')
# hoping to show if it's a prime number or not f(n) = n2 + n + 41
# def prime_calc():
#     prime=int(input("write the number you want to know if it's a prime number: "))
#     prime = 0
#     for i in prime:
#         calc=i^2 + i + 41
#         return calc
#         print(f'{calc}')


#multiply numbers
# def multipilaction_table():
#     num=(int(input("input the number you want to multiply: ")))
#     for i in range(1,13):
#         mul= num * i
#         print(f"{num} * {i} = {mul}")



# multipilaction_table()

#
# prime_calc()
prime_number()
# finding_largest_num()
# reverse_string()
# # is_palindrome("s")
# # sum_calc("n")
