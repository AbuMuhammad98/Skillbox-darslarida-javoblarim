friend = int(input("Do'stlar sonini kiriting: "))

def Friends_list(friend):
    friends = []
    for i in range(friend):
        friends.append(0)
    return friends

friends = Friends_list(friend)
lending_credits = int(input("Qarz tilxatlari: "))

def Led_Borrowed(lending_credits):
    for number in range(lending_credits):
        print(f'\n{number + 1}  - tilxat')
        to_who = int(input('kimga: '))
        from_who = int(input('Kimdan: '))
        how_much = int(input('Qancha: '))
        friends[from_who - 1] += how_much
        friends[to_who - 1] -= how_much

Led_Borrowed(lending_credits)

def Balans(friends):
    print("\nDo'stlaer xisobi:")
    for index in range(len(friends)):
        print(f'{index + 1} : {friends[index]}')

Balans(friends)
