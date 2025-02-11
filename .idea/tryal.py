#ADDITTION
def add():
    num1 = int(input("enter a number: "))

    while True:
        num2 = int(input("enter another number: "))
        ask = input("will you like to add another number (y/n): ")
        answer = {num1 + num2}

        if ask == "n":
            print(f"{num1} + {num2} = {num1 + num2}")
            break
        elif ask == "y":
            if 'y' ==



add()