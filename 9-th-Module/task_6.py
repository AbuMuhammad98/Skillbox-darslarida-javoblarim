print('6-topshiriq. Maxsus shifr')

# Nima qilish kerak

# Maxsus xizmatlarning ikki xodimi g'ayrioddiy shifr bilan yozishmalar olib borishmoqda. Ular har bir harfni satr shaklida shifrlashadi, uning ichida "s" harflarining uzun ketma - ketligi mavjud va eng uzunining uzunligi  - ular yubormoqchi bo'lgan alifbo harfining raqamidir.
# Kirish uchun satrni oladigan, unda ketma-ket keluvchi  "s" harflarining eng uzun ketma-ketligini hisoblaydigan va javobni ekranga chiqaradigan dasturni yozing.

# Misol:
# Qatorni kiriting: ssbbbsssbc
# Eng uzun ketma-ketlik: 3
shifr = input("Qatorni kiritng: ")
s_uzun = 0
s = 0
for harf in shifr:
  if harf == 's':
    s += 1
    # print(f"s: {s}")
  elif s > s_uzun:    
    s_uzun = s
    s = 0
    # print("s_uzun", s_uzun)
print(f"Eng uzun ketma-ketlik: {s_uzun}")
