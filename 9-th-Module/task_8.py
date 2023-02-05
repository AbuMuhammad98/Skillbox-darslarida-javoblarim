print('8-topshiriq. Коlontitul')

# Nima qilish kerak

# Muhim e'lonlarni chop etish uchun dastur yozishimiz kerak. Bunday e'lonning yuqori qismida mana bunday kolontitul joylashgan bo'lishi kerak:
#  ~~~~~~~~~~!!!!!!~~~~~~~~~~
# Undov belgilari har doim chiziqning markazida joylashib, e'lonning ahamiyatiga qarab undov belgilarining soni har xil bo'lishi mumkin. Avval foydalanuvchidan belgilardagi kolontitulning umumiy uzunligini, so'ngra undov belgilarining kerakli miqdorini so'raydigan, shundan so'ng u tayyor qatorni ko'rsatadigan dasturni yozing.
belgi  = int(input("Kolontitulning umumiy uzunligi: "))
belgi1 = int(input("Undov belgisining kerakli miqdori: "))
for kontitul in range(1):
  print("~" * belgi + '!' * belgi1 + "~" * belgi)
