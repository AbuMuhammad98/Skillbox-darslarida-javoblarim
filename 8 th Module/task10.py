print('10-topshiriq. Kinoteatr')

# Nima qilish kerak

# X o'g'il bolalar va Y qiz bolalar kinoteatrga borib, bitta qatordan ketma-ket  o'rindiqlar uchun chiptalarni sotib olishdi. O'g'il va qizlar bolalarga qanday o'tirish kerakligini ko'rsatadigan dastur yozing, shunda har bir o'g'il bolaning yonida kamida bitta qiz, har bir qizning yonida kamida bitta o'g'il bo'lishi kerak.
# Kirish uchun ikkita raqam beriladi: X  - o'g'il bolalar soni x va Y - qizlar soni. Javobda masalaning shartini qondiradigan aniq X belgilar B (o'g'il bolalarni bildiruvchi) va Y belgilar G (qizlarni bildiruvchi) bo'lgan qatorni ko'rsating. Belgilar orasidagi bo'shliqlarni ko'rsatish kerak emas. Agar  o'g'il va qizlarni masalaning shartiga ko'ra o'tqizish imkoni bo'lmasa, "Yechim yo'q" xabarini  chop eting.

# 1-misol:

# O'g'il bolalar sonini kiriting: 5
# Qizlar sonini kiriting: 5
# Javob: BGBGBGBGBG

# 2-misol:

# O'g'il bolalar sonini kiriting: 5
# Qizlar sonini kiriting: 3 
# Javob: BGBGBBGB

# 3-misol:

# O'g'il bolalar sonini kiriting: 100
# Qizlar sonini kiriting: 1
# Javob: Yechim yo'q
x = int(input("O'g'il bolalar sonini kiriting: "))
y = int(input("Qizlar sonini kiriting: "))
javob = ''
if x > 2 * y or y > 2 * x:
  print("Yechim yo'q")

else:
  for i in range(x+y):
    if x > y:
      javob += 'BGB'
      x -= 2
      y -= 1
    elif x < y:
      javob += 'GBG'
      x -= 1
      y -= 2
    elif x == y and x:
      javob += 'BG'
      x -= 1
      y -= 1

print(f"Javob: {javob}")