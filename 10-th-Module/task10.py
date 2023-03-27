print('10-vazifa. Chuqur')

# Nima qilish kerak

# Siz matnli grafikaga ega kompyuter o'yinini yaratyapsiz, sizga landshaft generatorini yozish topshirildi.
# Quyidagicha kirishda N raqamini qabul qiladigan va raqamlarni shunday “chuqur” ko‘rinishida ekranda ko‘rsatadigan dasturni tuzing:

# Raqam kiriting: 5

# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345
n = int(input('Raqamni kiriting: '))
for x in range(n, 0, -1):
  for y in range(n, 0, -1):
    if x - 1 < y:
      print(y, end='')
    else:
      print('.', end='')
  for y in range(1, n + 1):
    if x - 1 < y:
      print(y, end='')
    else:
      print('.', end='')
  print()