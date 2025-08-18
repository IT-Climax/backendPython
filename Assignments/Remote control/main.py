import json


class TV:
    def __init__(tv):
        tv.is_on = False
        tv.volume = 10
        tv.channel_list = [
            {"name": "CNN", "channel_number": 1},
            {"name": "TVC News", "channel_number": 2},
            {"name": "NTA", "channel_number": 3},
            {"name": "Arise News", "channel_number": 4},
            {"name": "NTA Sport", "channel_number": 5}
        ]
        tv.channel = tv.channel_list[0]  # Default channel is CNN

    def power(tv):
        """Toggle TV power."""
        tv.is_on = not tv.is_on
        state = "TV ON" if tv.is_on else "TV OFF"
        print(state)

    def change_channel(tv, channel_number):
        """Change TV channel."""
        if tv.is_on:
            for channel in tv.channel_list:
                if channel['channel_number'] == channel_number:
                    tv.channel = channel
                    print(f"Changed to channel {tv.channel['name']} (Channel {tv.channel['channel_number']}).")
                    return
            print("Invalid channel number.")
        else:
            print("TV is OFF. Please turn it on first.")

    def volume_up(tv):
        """Increase volume by 1%."""
        if tv.is_on:
            tv.volume += 1
            (print(f"Volume increased to {tv.volume}%."))
        else:
            print("TV is OFF. Please turn it on first.")

    def volume_down(tv):
        """Decrease volume by 1%."""
        if tv.is_on:
            tv.volume -= 1
            print(f"Volume decreased to {tv.volume}%.")
        else:
            print("TV is OFF. Please turn it on first.")

def display_menu():
    """Display menu of options to the user."""
    print("\nTV Remote Control")
    print("0: To Power On/Off TV")
    if tv.is_on:
        # Only show other options if the TV is ON
        print("2. Change Channel")
        print("3. Volume Up")
        print("4. Volume Down")
    print("5. Exit")

def main():
    global tv
    tv = TV()

    while True:
        display_menu()
        choice = input("Enter your choice (0, 2, 3, 4, 5): ").strip()

        if choice == '0':
            tv.power()
        elif choice == '2' and tv.is_on:
            # Change channel works only if TV is on
            print("\nAvailable Channels:")
            for channel in tv.channel_list:
                print(f"Channel {channel['channel_number']}: {channel['name']}")
            channel_num = int(input("Enter channel number to switch to: "))
            tv.change_channel(channel_num)
        elif choice == '3' and tv.is_on:
            tv.volume_up()
        elif choice == '4' and tv.is_on:
            tv.volume_down()
        elif choice == '5':
            print("Exiting remote control.")
            break
        else:
            print("Invalid option or TV is OFF. Please turn on the TV first.")

if __name__ == "__main__":
    main()
