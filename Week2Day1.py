football_players = ['Haaland', 'Messi', 'CR7', 'Neymar', 'Fabregas', 'Osime']

football_players.append('Lookman')
print(football_players)
print(football_players[5])
football_players[4] = "Yamal"
football_players.append('busola')
print(football_players)
football_players.remove('busola')
print(football_players)
print(len(football_players))
top_3 = football_players[1:3]

for players in football_players:

    if players == 'CR7':
        print(f"I am the greatest of all players")
    else:
        print(f"I am {players} the great player")

print(top_3)
def classwork():
    try:
        number = int(input("kindly enter a number: "))
        print(number)
    except ValueError:
        print("Kindly ensure you enetered a number")


# classwork()
