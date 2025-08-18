def calculation():
    while True:
            print('what will you like to do')
            list = ["addition","multiplication","division","subtraction","square"]
            print(f'{list}')
            command = input("> ")
            if command not in list:
                print (f"check your input")
            elif command.lower() == "addition":
                num = int(input("input the first number you want to calculate  "))
                numb = int(input("input the second number you want to calculate "))
                while True:
                    print(f"will you like to add more numbers ?")
                    ans = input ("> ")
                    if ans.lower() == "no":
                        compilation = num + numb
                        print(f"{num} + {numb} = {compilation}")
                    elif ans.lower()=="yes":
                        print(f"{num} + {numb}")
            elif command.lower() == "multiplication":
                mul = int(input("input the first number you want to calculate  "))
                mul2= int(input("input the first number you want to calculate  "))
                comp = mul * mul2
                print(f"{mul} * {mul2} = {comp}")
            elif command.lower() == "division":
                div = int(input("input the first number you want to calculate  "))
                div2 = int(input("input the first number you want to calculate  "))
                compile = div // div2
                print(f"{div} / {div2} = {compile}")
            elif command.lower() == "subtraction":
                sub = int(input("input the first number you want to calculate  "))
                sub2= int(input("input the first number you want to calculate  "))
                com = sub - sub2
                print(f'{sub} - {sub2} = {com}')
            elif command.lower() =="square":
                squ = int(input("input the number you want to calculate "))
                calc= squ ** squ
                print(f"the square root of {squ} = {calc}")
            print(" will you like to continue? ")
            response= input("> ")
            if response.lower() == "no":
                break



calculation()