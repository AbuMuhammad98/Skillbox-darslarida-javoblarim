print('7-topshiriq. Stipendiya')

# Nima qilish kerak

# Talabaning oylik stipendiyasi educational_grant rublni tashkil qiladi va yashash xarajatlari stipendiyadan oshib ketadi va oyiga expenses rublni tashkil qiladi. Oylik narxlarning ko'tarilishi birinchi oydan tashqari xarajatlarni 3 foizga oshiradi. O'quv yili (o'n oy) boshida  talabaning faqat shu pul va stipendiyadan foydalangan holda yashash uchun ota-onasidan bir marta olishi kerak bo'lgan pul miqdorini hisoblash dasturini tuzing.    

# Misol:

# Stipendiyani kiriting: 10000
# Yashash xarajatlarini kiriting: 13000
# Ota-onadan so'rashlari kerak: 49030.431

scholarship = int(input("Stipendiya miqdorini kiriting: "))
cost = int(input("Xarajatlar miqdorini kiriting: "))
scholarship_annual = 0
cost_annual = 0
parents_money = 0
 
for month in range(1, 11):
  if month == 1:
    scholarship_annual += scholarship
    cost_annual += cost
  elif month > 1:  
    scholarship_annual += scholarship
    cost *= 1.03 
    cost_annual += cost
    
  
print(f"Ota - onasidan so'rashlari {cost_annual-scholarship_annual}")


