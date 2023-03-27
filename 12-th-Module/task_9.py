import random


def mainMenu():
    pass
    # Bu yerda o'yinning asosiy menyusi
    print("1. Tosh, qaychi, qog'oz o'yini")
    print("2. Raqamni top o'yini")
    choise = int(input("Avval o'yinni tanlang: "))
    if choise == 1:
        rock_paper_scissors(satr)
    elif choise == 2:
        guess_the_number(number)
    else:
        print("Xato raqamni kiritdingiz. Tanlov faqat 1 va 2")


def rock_paper_scissors(satr):
    man = 0
    comp = 0
    print("Tosh, Qaychim, Qog'oz o'yiniga Xush Kelibsiz")
    while True:
        satr = random.choice(["Tosh", "Qaychi", "Qogoz"])
        # print(satr)
        user = input("(Tosh, Qaychi, Qogoz)-tanlang: ").title()
        if user == satr:
            print("Durrang")
            print()
            continue
        elif ((satr == "Tosh") and (user == "Qaychi")) or ((satr == "Qaychi") and (user == "Qogoz")) or ((satr == "Qogoz") and (user == "Tosh")):
            comp += 1
            print("Siz yutqazdingiz.")

            if comp == 3:
                print("Computer g'alaba qozondi")
                print(f"{man}:{comp}")
                comp = 0
                game = int(input("Davom ettiramizmi: 1-ha, 2-yo'q: "))
                if game == 1:
                    continue
                else:
                    mainMenu()
                print(f"{man}:{comp}")
                print()


        elif user == "Exit":
            mainMenu()

        elif ((satr == "Qaychi") and (user == "Tosh")) or ((satr == "Qogoz") and (user == "Qaychi")) or ((satr == "Tosh") and (user == "Qogoz")):
            man += 1
            print("Siz yutdingiz.")
            if man == 3:
                print("Foydalanuvchi g'alaba qozondi")
                print(f"{man}:{comp}")
                man = 0
                game = int(input("Davom ettiramizmi: 1-ha, 2-yo'q: "))
                if game == 1:
                    continue
                else:
                    mainMenu()

            print(f"{man}:{comp}")
            print()
        else:
            print("Noto'g'ri komanda kiritdingiz!!!")
            continue


def guess_the_number(number):
    man = 0
    comp = 0
    urinishlar_soni = 0
    print("Raqamni top o'yiniga Xush Kelibsiz")
    while True:

        num = int(input("Computer o'ylagan raqamni toping: "))
        if num == number:
            print("Javob to'g'ri. Foydalanuvchi yutdi")
            man += 1
            urinishlar_soni = 0
            number = number = random.randrange(0, 101)
            if man == 3:
                print("Foydalanuvchi g'alaba qozondi")
                print(f"{man}:{comp}")
                man = 0
                game = int(input("Davom ettiramizmi: 1-ha, 2-yo'q: "))
                if game == 1:
                    continue
                else:
                    break


        elif num > number:
            print(f"Raqam {num} dan kichik")
            urinishlar_soni += 1
        else:
            print(f"Raqam {num} dan katta")
            urinishlar_soni += 1
        if urinishlar_soni == 7:
            print("Urinishlar soni tugadi. Computer yutdi")
            comp += 1
            urinishlar_soni = 0
            number = number = random.randrange(0, 101)
            if comp == 3:
                print("Computer g'alaba qozondi")
                print(f"{man}:{comp}")
                comp = 0
                game = int(input("Davom ettiramizmi: 1-ha, 2-yo'q: "))
                if game == 1:
                    continue
                else:
                    break


satr = random.choice(["Tosh", "Qaychi", "Qog'oz"])
number = random.randrange(0, 101)
mainMenu()