print('1-vazifa. Sinov vazifasi')

# Nima qilish kerak

# Sanjar ishga joylashish uchun ish joyiga keldi va unga sinov vazifasi berildi:
# Quyidagi jadvalni tahlil qilish, u qanday tuzilganligini tushunish va uni ekranda aks ettirish uchun dasturni yozish.

# 0 2 4 6  8  10
# 1 3 5 7  9  11
# 2 4 6 8  10 12
# 3 5 7 9  11 13
# 4 6 8 10 12 14
# 5 7 9 11 13 15
# 
# Sanjarga bunday dasturni amalga oshirishga yordam bering.
# Ko’rsatma: ustunlar soni. Shuningdek, tabulyatsiya uchun \t literali haqida unutmang.
rows = int(input("Qator raqamni kiriting: "))
columns = int(input("Ustun raqamni kiriting: "))
for row in range(rows + 1):
  for col in range(columns + 1):
    if col % 2 == 0:
      print(col+row, ' ', end = '')
  print()