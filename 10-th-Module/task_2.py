print('2-vazifa. Zinapoya')

# Nima qilish kerak

# Foydalanuvchi N raqamini kiritadi. Raqamlardan shunday “narvonchani” aks ettiruvchi dasturni yozing:

# Raqamni kiriting: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
size = int(input("Raqamni kiriting: "))
for row in range(1, size + 1):
  for col in range(row):
    print(row, ' ', end = '')
  print()