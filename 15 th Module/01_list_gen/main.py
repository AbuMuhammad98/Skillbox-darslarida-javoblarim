def ToqSonlar(num):
    toq_sonlar = []
    for i in range(num + 1):
        if i % 2 == 1:
            toq_sonlar.append(i)
    return print(f"Birdan {num} gacha bo'lgan toq_sonlar ro'yxati: {toq_sonlar}")
num = int(input("Butun sonni kiriting: "))
ToqSonlar(num)
