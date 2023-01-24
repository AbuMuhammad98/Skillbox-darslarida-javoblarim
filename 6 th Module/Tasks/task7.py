print("Sakkiz soatlik kun boshlandi")
soat = 0
vazifalar_soni = 0
while True:
  print(f"{soat+1}-soat")
  vazifa = int(input("Bobur nechta vazifani bajardi?: "))
  telefon = input("Xotini qo’ng’iroq qilmoqda. Javob berish kerakmi? (1 —ha, 0 —yo'q): ")
  soat+=1
  vazifalar_soni +=vazifa
  if telefon != 0:
    ha = "Do'konga borish kerak"
  if soat == 8:
    print(f"Ish vaqti tugadi. Jami bajarilgan vazifalar soni: {vazifalar_soni}")
    print(ha)
    break