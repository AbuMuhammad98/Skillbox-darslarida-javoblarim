guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f"Hozir bayramda kechasida {len(guests)} kishi: {guests}")
    answer = input("Mehmon keldimi yoki ketdimi: ").lower()
    if answer == 'keldi':
        name_g = input("Mehmonni ismi: ").title()
        if len(guests) < 6:
            guests.append(name_g)
            print(f"Salom {name_g}")
        else:
            print(f"Uzr, {name_g}, lekin joy yo'q")
    elif answer == 'ketdi':
        name_g = input("Mehmonni ismi: ").title()
        guests.remove(name_g)
        print(f"Xayr, {name_g}")
    elif answer == 'uxlash vaqti boldi':
        print('Bazm kechasi tugadi hamma uxlashga yotdi')
        break