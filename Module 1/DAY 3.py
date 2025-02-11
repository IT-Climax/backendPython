football_players = ['Haaland', 'Messi', 'CR7', 'Neymar', 'Fabrigas', 'Osimhen']
football_players.append('lookman')
print(football_players)
football_players[4]= 'Yamal'
football_players.append ('busola')
football_players.remove('busola')
print(football_players)
top_3 = football_players[1:3]

for players in football_players:
    if players == 'CR7':
        print(f'I am the greatest of all players')
    else:
        print(f'I am {players} the greatest player')





