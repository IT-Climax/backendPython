file_name="princess_practice.txt"
with open (file_name,"w")as file:
    file.write("welcome to another wonderful day hope you have a lovely day \n we are glad you could join us on this journey")
with open(file_name,"r")as file:
    content=file.read()

    print(content)
while True:
    name=input("please enter your name:")
    if name.isalpha():
        print(f"we are glad to have you {name} we hope to serve you well ")
        break
    else:print("please enter letters only please")
