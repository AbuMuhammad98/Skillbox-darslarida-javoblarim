players = ['Temur', 'Muhtor', 'Amir', 'Siroj', 'Aziz', 'Farruh', 'Kamola', 'Sitora']
first_day = []
second_day = []
def juft_ishtirokchilar(players):
    players_count = len(players)
    for player in range(1, players_count + 1):
        if player % 2 == 0:
            first_day.append(players[player - 2])
    return f"Birinchi kun: {first_day}"


print(juft_ishtirokchilar(players))
