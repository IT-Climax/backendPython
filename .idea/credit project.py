def word():
    try:
        name = input("please input your name:  ")
        length = len(name)
        if length < 3:
            print(f"name too short")
        elif length > 50:
            print(f"name too long")
        else:
            print(f"good name")
    except ValueError:
        print(f"please insert an string and not an integer")


numbers = [2,2,2,2,6]
for number in numbers:
        output = ''
        for item in range (number):
            output += 'X'
        print(output)
#word()