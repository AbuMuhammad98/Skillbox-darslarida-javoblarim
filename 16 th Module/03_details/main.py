shop = [['siljima qism', 1200], ['shatun', 1000], ["o'rindiq", 300],
        ['tepki', 100], ["o'rindiq", 1500], ['rama', 12000],
        ['gardish', 2000], ['shatun', 200], ["o'rindiq", 2700]]
detal_name = input("Detalning nomi: ").lower()
count = 0
summ = 0
for detals in shop:
    if detals[0] == detal_name:
            count += 1
            summ += detals[1]

if count > 0:
    print(f"detallar soni: {count} ta")
    print(f"Umumiy narxi: {summ}")
else:
    print("Bunday mahsulot yo'q")

