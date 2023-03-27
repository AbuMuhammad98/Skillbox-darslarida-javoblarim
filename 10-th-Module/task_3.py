print('3-vazifa. Ramka')

# Nima qilish kerak

# Simvolli grafiklardan foydalanib to‘rtburchak shakldagi ramkani chizuvchi dasturni tuzing. Vertikal chiziqlar uchun vertikal chiziq belgisi- | dan foydalaning, gorizontal chiziqlar uchun – defis - dan foydalaning. Foydalanuvchi ramkaning kengligi va balandligini kiritsin.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|
rows = int(input("Qatornig uzunligini kiriting: "))
columns = int(input("Ustunnig uzunligini kiriting: "))
for row in range(rows + 1):
  for col in range(columns + 1):
    if row == 0:
      print("-", end = "")
    elif row == rows:
      print("-", end = "")
    elif col == 0:
      print("|", end = "")
    elif col == columns:
      print("|", end = " ")
    else:
      print(" ", end = '')
  print()