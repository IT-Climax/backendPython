username=input("enter your name:")
print("hello "+username)

age=int(input("enter your age:"))
weight=int(input("enter your weight:"))
sex= input("enter your sex(male/female):").lower()

def under_weight():
    A="""you are advised to 
    1.Eat a proper diet
    2.Have plenty of rest
    3.reduce stressful situation
    4.sleep at least 8hrs a day
        you are also advised to seek help for a medical personelle if all these do not work."""
    print(A)
def over_weight():
    B="""you are advised to
    1.Eat food with little calories
    2. drink alot of water
    3.exercise daily
    4.avoid binge eating
    regularly visit the hospital to check your weight
    consult a dietiian."""
    print(B)




if sex=="male":
    if age in range(10,19):
        if 45<=weight<=60:
            print("congratulation"+username,"you are perfectly healthy")
        elif weight<45:
            print(username + "you are underweight")
            x=input(username+"would you like guidelines to help gain weight: ")
            if x=="yes":
                under_weight()
                y=input("was this helpful(yes/no):").lower()
                if y=="yes":
                    print("i'm glad i could help")

                else:
                    print("sorry i wasnt of any help")
            else:
                print("thank you" + username)

        else:
            print(username+"you are over weight")
            q=input(username +"would like guidelines to help loose weight: ")
            if q=="yes":
                over_weight()
                a= input("was this helpful(yes/no):").lower()
                if a == "yes":
                    print("i'm glad i could help")
                else:
                    print("sorry i wasnt of any help")
            else:
                print("thank you" + username)


    elif age in range(5,10):
        if 15 <= weight <= 35:
            print("congratulation" + username, "you are perfectly healthy")
        elif weight < 15:

            print(username + "you are underweight")
            x = input(username + "would you like guidelines to help gain weight: ")
            if x == "yes":
                under_weight()
                y = input("was this helpful(yes/no):").lower()
                if y == "yes":
                        print("i'm glad i could help")

                else:
                 print("sorry i wasnt of any help")
        else:
            print("thank you" + username)

    else:
        print(username + "you are over weight")
        q = input(username + "would like guidelines to help loose weight: ")
        if q == "yes":
            over_weight()
            a = input("was this helpful(yes/no):").lower()
            if a == "yes":
                print("i'm glad i could help")
            else:
                print("sorry i wasnt of any help")
        else:
            print("thank you" + username)






    if age in range(19,36):
        if 67<=weight<=88:
            print("congratulation"+username,"you are perfectly healthy")
        elif weight<67:
            print(username + "you are underweight")
            x=input(username+"would you like guidelines to help gain weight: ")
            if x=="yes":
                under_weight()
                y=input("was this helpful(yes/no):").lower()
                if y=="yes":
                    print("i'm glad i could help")
                else:
                    print("sorry i wasnt of any help")
            else:
                print("thank you" + username)

        else:
            print(username+"you are over weight")
            q=input(username +"would like guidelines to help loose weight: ")
            if q=="yes":
                over_weight()
                a= input("was this helpful(yes/no):").lower()
                if a == "yes":
                    print("i'm glad i could help")
                else:
                    print("sorry i wasnt of any help")
            else:
                print("thank you" + username)

    if age in range(36,51):
        if 59<=weight<=75:
            print("congratulation"+username,"you are perfectly healthy")
        elif weight<59:
            print(username + "you are underweight")
            x=input(username+"would you like guidelines to help gain weight: ")
            if x=="yes":
                under_weight()
                y=input("was this helpful(yes/no):").lower()
                if y=="yes":
                    print("i'm glad i could help")
                else:
                    print("sorry i wasnt of any help")
            else:
                print("thank you" + username)

        else:
            print(username+"you are over weight")
            q=input(username +"would like guidelines to help loose weight: ")
            if q=="yes":
                over_weight()
                a= input("was this helpful(yes/no):").lower()
                if a == "yes":
                    print("i'm glad i could help")
                else:
                    print("sorry i wasnt of any help")
            else:
                print("thank you" + username)

    if  51<=weight<=70:
         print("congratulation"+username,"you are perfectly healthy")
    elif weight<45:
            print(username + "you are underweight")
            x=input(username+"would you like guidelines to help gain weight: ")
            if x=="yes":
                under_weight()
                y=input("was this helpful(yes/no):").lower()
                if y=="yes":
                    print("i'm glad i could help")
                else:
                    print("sorry i wasnt of any help")
            else:
                print("thank you" + username)

    else:
            print(username + "you are over weight")
            q=input(username + "would like guidelines to help loose weight: ")
            if q=="yes":
                over_weight()
                a= input("was this helpful(yes/no):").lower()
                if a == "yes":
                    print("i'm glad i could help")
                else:
                    print("sorry i wasnt of any help")
            else:
                print("thank you" + username)






    if age>=70:
        if 70<=weight<=80:
            print("congratulation"+username,"you are perfectly healthy")
        elif weight<45:
            print(username + "you are underweight")
            x=input(username+"would you like guidelines to help gain weight: ")
            if x=="yes":
                under_weight()
                y=input("was this helpful(yes/no):").lower()
                if y=="yes":
                    print("i'm glad i could help")
                else:
                    print("sorry i wasnt of any help")
            else:
                print("thank you" + username)

        else:
            print(username+"you are over weight")
            q=input(username +"would like guidelines to help loose weight: ")
            if q=="yes":
                over_weight()
                a= input("was this helpful(yes/no):").lower()
                if a == "yes":
                    print("i'm glad i could help")
                else:
                    print("sorry i wasnt of any help")
            else:
                print("thank you" + username)

