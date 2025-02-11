def add_numbers():
    total = 0
    while True:
        user_input = input("enter a number to add or 'q' to quit")
        if user_input.lower() == "q":
            print(f"final total: {total}")
            break
        try:
            num= float(user_input)
            total += num
            print(f'running total {total}')
        except ValueError:
            print(f"invalid input. please enter a number or q to quit")

add_numbers()
