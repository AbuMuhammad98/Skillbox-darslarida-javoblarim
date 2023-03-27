print('1-topshiriq. Konvertasiya')

# Nima qilish kerak?

# Chet elda xarid qilayotganda karta yordamida banklar oraliq valyuta orqali konvertasiyani amalga oshiradilar.

# Misol uchun, agar siz yevroda biror narsa sotib olsangiz, avvalo bu miqdor dollarga, keyin esa rublga aylantiriladi.

# Xarid narxini yevroda qabul qiluvchi, so‘ngra javobni rublda chiqaradigan dastur yozing. Biz 1 yevro = 1,25 dollar, 1 dollar esa = 60,87 rubl bo‘lgan muqobil voqelikda yashayapmiz.
evro = float(input("Qancha yevro konvertatsiya qilmoqchisiz: "))
dollar = evro * 1.25
rubl = dollar * 60.87
print(f"Siz kiritgan {evro} evro, {round(rubl, 1)} rublni tashkil qiladi")
