print('3-topshiriq. Egri xabarchi')

# Nima qilish kerak

# Xabarlarni bitta messenjer orqali uzatishda ba'zida muammolar paydo bo'ladi va xabar qo'shimcha belgi - yulduzchaga tushadi. Foydalanuvchilar bundan juda charchashdi va  boshqa messenjerlarga o'tishni boshladilar. Foydalanuvchilardan biri ushbu yulduz odatda qanday pozitsiyalarda paydo bo'lishi bilan qiziqib qoldi.
# Buni bilish uchun foydalanuvchi "*" belgisi aniq bir marta paydo bo'ladigan satrlarni ishlab chiqishi kerak. Satrda ushbu belgining tartib raqamini aniqlaydigan dastur yozing.

# Misol:
# Matnni kiriting: Sa*lom qandaysiz
# ‘*’ belgisi  3-pozitsiyada joylashadi. 
matn = input("Matnni kiriting: ")
pozitsiya = 0
for belgi in matn:
  pozitsiya += 1
  if belgi == '*':
    print(f"'*' belgisi {pozitsiya} da joylashadi.")