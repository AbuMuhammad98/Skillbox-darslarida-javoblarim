import random as r

first_team = [round(r.uniform(5.0, 10.0), 2) for _ in range(20)]
second_team = [round(r.uniform(5.0, 10.0), 2) for _ in range(20)]
winner = [(first_team[i] if first_team[i] > second_team[i] else second_team[i]) for i in range(20)]
print(f"Birinchi jamoa: {first_team}")
print(f"Ikkinchi jamoa jamoa: {second_team}")
print(f"Davra g'oliblari: {winner}")




