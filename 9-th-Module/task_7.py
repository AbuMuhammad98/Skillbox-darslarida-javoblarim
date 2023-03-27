print('7-topshiriq. Buyuk va qudratli')

# Nima qilish kerak

# Sardor rus tilini o'rganmoqda: u darsliklar bo'yicha shug'ullanadi, kitob o'qiydi, musiqa tinglaydi. Sardorga, ayniqsa, "Jinoyat va jazo" kitobi yoqib qoldi. U keyin uni o'z tilidagi o'xshash so'z bilan taqqoslash uchun ushbu kitobdagi eng uzun so'zni qanday topishga qiziqdi.
# Matnni kiritadigan va undagi eng uzun so'zning uzunligini topadigan dastur yozing. Matndagi so'zlar bitta bo'sh joy bilan ajratiladi.

# Misol:
# Matnni kiriting: mening ismim Pyotr
# Eng uzun so'zning uzunligi: 5

matn = input("Matnni kiriting: ")
eng_uzun = 0
harflar_soni = 0
for harf in matn:
  
  if harf != ' ':
    harflar_soni += 1   
  else:
      if harflar_soni > eng_uzun:
        eng_uzun = harflar_soni
      harflar_soni = 0

    
    
print(f"Eng uzun so'zning uzunligi: {eng_uzun}")

