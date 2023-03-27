print('3-topshiriq. Qotil Steam')

# Nima qilish kerak?

# Siz kompyuter o‘yini uchun installyator-dasturni yozayapsiz. Installyator yangilashni yuklab bo‘lguncha, foydalanuvchi choy tayyorlashga yoki kompyuter ekrani oldida kutishga qaror qilishi uchun qancha foiz yuklab olinganligini ko‘rsatish kerak. O‘yin yangilashlari har doim turlicha megabaytni oladi, o‘yinchilarning Internetga ulanish tezligi ham har xil.
# Yangilash faylining o‘lchamini megabaytlarda va Internetga ulanish tezligini sekundiga megabaytlarda kiritishni qabul qiladigan dastur yozing. Har bir sekund uchun dastur butun hajmda yuklab olinmaguncha, umumiy hajmning necha foizi yuklab olinganligini hisoblab chiqadi va ekranga chiqaradi. Oxirida dastur yangilashni yuklab olish uchun necha sekund vaqt ketganini ko‘rsatishi kerak. Kirish nazoratini ta’minlang.

# Misol:

# Yuklab olish uchun fayl hajmini ko‘rsating: 123
# Ulanish tezligingiz qanday? 27
 
# 1 sekund o‘tdi. 123 MBdan 27 MB yuklab olindi (22%)
# 2 sekund o‘tdi. 123 MBdan 54 MB yuklab olindi (44%)
# 3 sekund o‘tdi. 123 MBdan 81 MB yuklab olindi (66%)
# 4 sekund o‘tdi. 123 MBdan 108 MB yuklab olindi (88%)
# 5 sekund o‘tdi. 123 Mb dan 123 MB yuklab olindi (100%)
import math as m
dastur_hajmi = float(input("Yuklab olish uchun fayl hajmini ko‘rsating: "))
i_tezlik = float(input("Ulanish tezligingiz qanday? "))
umumiy_vaqt = int(m.ceil(dastur_hajmi / i_tezlik))
yuklanish = 0
foiz = 0
for sekund in range(1, umumiy_vaqt + 1):
  yuklanish += i_tezlik
  foiz += ((i_tezlik * 100) / dastur_hajmi)
  if foiz > 100:
      foiz += 100 - foiz
  if yuklanish > dastur_hajmi:
    yuklanish += dastur_hajmi - yuklanish
  print(f"{sekund} sekund o'tdi. {dastur_hajmi} MBdan {round(yuklanish, 2)} MB yuklab olindi ({round(foiz, 1)}%)")
  a = 'Hammaga rahmat'
  print()
  m.c