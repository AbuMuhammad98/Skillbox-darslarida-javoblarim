print('5-topshiriq. Funktsiya 2')

# Nima qilish kerak

# Oxirgi marta biz Boburga kesimning har bir nuqtasida funktsiyani hisoblaydigan va oxiridan boshlab - kattaroq X qiymatidan kichikroqgacha kerakli qadam bilan bo'lgan,  javobni ekranda aks ettiradigan dasturni yozdik. Ammo endi Boburga qiymatlar teskari tartibda hisoblanishi kerak. Shuningdek, Bobur uchun kesimning nuqtalari bo'ylab harakatlanadigan qadamni sozlash juda muhim.
# Kirish uchun kesimning boshi va oxirini, shuningdek qadamni oladigan dasturni yozing. Keyin kesimning har bir nuqtasida igrek funktsiyasini hisoblab chiqsini va oxiridan boshlab kerakli qadam bilan javobni ekranga chiqarsin.

# Funktsiyaning o'zi quyidagicha ko'rinishga ega:
# y = x**3 + 2 * x**2 - 4x + 1

# Misol:

# Kesimning boshini kiriting: -2
# Kesimtning oxirini kiriting: 2
# Qadamni kiriting: -1
# 2-nuqtada funktsiya 9 ga teng
# 1-nuqtada funktsiya 0 ga teng
# 0 nuqtada funktsiya 1 ga teng
# -1 nuqtada funktsiya 6 ga teng
# -2 nuqtada funktsiya 9 ga teng

# Maslahatlar va tavsiyalar
# range(start, stop) funktsiyasi stop chegarasini o'z ichiga olmaydi, unga etib bermasdan to'xtaydi.

start = int(input("Kesimning boshini kiriting: "))
stop = int(input("Kesimning oxirini kiriting: "))
step = int(input("Qadamni kiriting: "))

for x in range(stop, start-1, step):
  y = x ** 3 + 2 * x ** 2 - 4 * x + 1
  print(f"{x} - nuqtada funktsiya qiymati: {y} ga teng")