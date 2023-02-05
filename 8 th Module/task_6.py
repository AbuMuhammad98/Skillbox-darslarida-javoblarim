print('6-topshiriq. Xat')

# Nima qilish kerak

# Bizda 12x12 santimetr o'lchamdagi kvadrat konvert va konvertga sig'maydigan kvadrat qog'ozdagi xat bor. Xatni konvertga sig'dirish uchun necha marta yarmiga katlash kerakligini aytadigan dastur yozing. Xatning o'lchamlari klaviaturadan kiritiladi.

# Maslahatlar va tavsiyalar
# Varaq kvadrat ekanligiga e'tibor bering.
# 12x12 o'lchamdagi varaq 12x12 konvertga erkin kirishini qabul qilamiz

a = int(input("Xatning o'lchami: "))
count = 0
step = a // 2
for i in range(a, 13, -step):
  count += 2
  
print(f"Taklamlar soni: {count} ta bo'lishi kerak")
  