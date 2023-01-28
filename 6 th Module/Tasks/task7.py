print("Sakkiz soatlik kun boshlandi")
soat = 0
vazifalar_soni = 0
go_to_store = 0
while soat != 8:
  print(f"{soat + 1} - soat")
  vazifa = int(input("Bobur nechta vazifani bajardi?: "))
  telefon = int(input("Xotini qo’ng’iroq qilmoqda. Javob berish kerakmi? (1 — ha, 0 — yo'q): "))
  soat += 1
  vazifalar_soni += vazifa
  if telefon == 1:
    go_to_store += 1
print(f"Ish vaqti tugadi. Jami bajarilgan vazifalar soni: {vazifalar_soni}")
if go_to_store >= 1:
      ha = "Do'konga kirish kerak"
      print(ha)