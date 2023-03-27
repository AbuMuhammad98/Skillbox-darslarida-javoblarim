print('7-topshiriq. Tuxum')

# Nima qilish kerak?

# Marsni mustamlaka qilish dasturi doirasida «Speis Injiniring» kompaniyasi toshbaqalarning maxsus zotini yaratdi, ular rejalashtirilganidek, mars tuprog’ida tuxum qo‘yib ko‘payishi kerak. Tuxumni yuzaga juda yaqin qo‘yish - radiatsiya tufayli va juda chuqur qo‘yish esa - tuproq bosimi va kislorod yetishmasligi tufayli xavfli.
# Umuman olganda, omillar juda ko‘p, ammo mutaxassislar juda ko‘p ish qilishdi va toshbaqa tuxumlari uchun xavf darajasini 
# D = x**3 − 3x**2 − 12x + 10 formulasi bilan hisoblash mumkinligini taxmin qilishdi, 
# bu yerda x - tuxum qo‘yish chuqurligi, metrda, D esa - xavf darajasi, shartli birliklarda. Gipotezani sinab ko‘rish uchun formuladagi xavfsiz chuqurlikka asosan tuproq namunasini olish kerak.
# Xavf darajasi imkon qadar nolga yaqin bo‘lgan x chuqurlikning qiymatini topuvchi dastur yozing. Xavf darajasining noldan maksimal ruxsat etilgan og’ishi dasturga kiritishda kiritiladi, dastur esa bu og’ishni qanoatlantiradigan x ning taxminiy qiymatini hisoblashi kerak. Ma’lumki, chuqurlik aniq noldan katta va to‘rt metrdan kam. Kirish nazoratini ta’minlang.

# Misol:

# Maksimal ruxsat etilgan xavf darajasini kiriting: 0.01 
# Taxminiy xavfsiz tuxum qo‘yish chuqurligi: 0.732421875 m
max_danger = float(input('Maksimal ruxsat etilgan xavf darajasini kiriting: '))

d_from = 0
d_to = 4
depth = d_from + (d_to - d_from) / 2
danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

if max_danger < 0:
    print('0 da katta raqam kiriting')
while abs(danger) > max_danger:
      if danger > 0:
        d_from = depth
      else:
        d_to = depth
      depth = d_from + (d_to - d_from) / 2
      danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
print(f"Depth: {depth} Danger: {danger}")
print(f"Taxminiy xavfsiz tuxum qo‘yish chuqurligi:  {depth} m")