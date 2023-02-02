print("8-topshiriq. Qator yig'indisi")

# Nima qilish kerak

# n natural son berilgan. Qatorning keyingi yig'indisini (birdan boshlab) hisoblash uchun dastur yozing:

# # S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N 

# Ta'rifsiz chiqishga ruxsat beriladi, qatorning yig'indisini ko'rsatishning o'zi kifoya.

# Maslahatlar va tavsiyalar
# Diqqat qiling: agar biz qator a'zosini  hisoblash uchun formuladan foydalansak, unda 
# n = 0 bo'lsa, qator a’zosi 1 ga teng; 
# n = 1 bo'lsa,   -1/2 ga ega bo’lamiz; 
# n = 2 bo’lgan holda 1/4 ni olamiz; 
# n = 3 bo’lsa  -1/8 bo’ladi.

number = int(input("n natural sonni kiriting: "))
s = 0
for n in range(0, number+1):
  if n == 0:
    s += 1
  else:
    s =(-1)**n * 1/2**n 
print(s)