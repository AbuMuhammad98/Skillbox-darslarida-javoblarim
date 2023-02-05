print('5-topshiriq. Marsoxod 2')

# Nima qilish kerak

# Robot Valliga yana bir robot-Billi yuborildi. Bu uning Marsga birinchi qo'nishi, shuning uchun u 15 metrdan 20 metrgacha bo'lgan to'rtburchak xonada sinovdan o'tkazilmoqda.  Marsoxod xonaning o'rtasiga (8, 10 nuqtada) tushiriladi, shundan so'ng uni boshqarish dastur operatori - foydalanuvchiga o'tkaziladi. 

# Dastur operator robotni qaysi tomonga yo'naltirishni xohlashini so'raydi: 
# shimol (W tugmasi), 
# janub (S tugmasi), 
# g'arb (A tugmasi) 
# yoki sharq (D tugmasi).  

# Operator tanlovni amalga oshiradi, marsoxod bu yo'nalishda 1 metrga harakatlanadi  va dastur marsoxodning yangi pozitsiyasini bildiradi. Agar marsoxod devorga taqalib qolsa, u devor tomon harakatlanmasligi kerak, bu holda uning pozitsiyasi o'zgarmaydi. Robot Billini boshqarish uchun dastur yarating.

# Misol:

# [Dastur]: Marsoxod 6, 19 pozitsiyasida joylashgan, buyruqni kiriting:
# [Оperator]: A
# [Dastur]: Marsoxod 5, 19, pozitsiyasida joylashgan, buyruqni kiriting: 
# [Оperator]: W
# [Dastur]: Marsoxod 5, 20, pozitsiyasida joylashgan, buyruqni kiriting:
# [Оperator]: W
# [Dastur]: Марсоход находится на позиции 5, 20, введите команду:

# Maslahatlar va tavsiyalar
# Chegaralarga e'tibor berish kerak.
x = 7
y = 15
for xona in range(100):
  print(f"Marsoxod {x}, {y} pozitsiyasida joylashgan, buyruqni kiriting :")
  buyruq = input("Buyruq: ").title()
  if buyruq == 'W':
     y += 1
     if y > 20:
       y = 20
  elif buyruq == 'S':
    y -= 1
    if y < 1:
      y = 1
  elif buyruq == 'A':
    x -= 1
    if x < 1:
      x = 1
  elif buyruq == 'D':
    x += 1
    if x > 15:
      x = 15