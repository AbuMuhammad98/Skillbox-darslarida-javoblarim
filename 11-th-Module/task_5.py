print('5-topshiriq. Mana buni hajm desa bo‘ladi!')

# Nima qilish kerak?

# Fizika bo‘yicha kurs ishi uchun Anvar ikkita sayyoraning hajmini solishtirishi kerak: Yer va nazariy jihatdan koinotimizda mavjud bo‘lishi mumkin bo‘lgan qandaydir tasodifiy sayyorani. Anvar formulalarni yaxshi biladi, lekin biror narsani hisoblash, ayniqsa,  o‘zi hisoblashi - unga yot narsa. Yerning hajmi unga oldindan ma’lum, bu - 10.8321 * 10 ** 11 km3.
# Ammo tasodifiy sayyoraning hajmini hisoblab topishi kerak bo‘ladi. Yaxshiyamki, unda quyidagi formula bor:

# # V = 4/3 πR ** 3

# Bu yerda V - hajm, π – pi soni,  R esa – sayyoraning radiusi.
# Kirishda tasodifiy sayyora radiusini qabul qiladigan va Yer sayyorasining hajmi undan necha marta kichikroq yoki kattaroq ekanligini ko‘rsatadigan dastur yozing. Javobingizni verguldan keyin uchta songacha yaxlitlang

# Misol:
# Tasodifiy sayyora radiusini kiriting: 3389.5
# Yer sayyorasining hajmi 6.641 marta katta

# 2-misol:
# Tasodifiy sayyora radiusini kiriting: 7000
# Yer sayyorasining hajmi (1/0.754) marta kichik  = 1.326 
r_sayyora = float(input("Taxminiy sayyoraning radiusini kiriting: "))
v_yer = 10.8321 * 10 ** 11
pi = 3.141592653589793
v = (4 / 3) * pi * (r_sayyora ** 3)
farq = round(v_yer / v, 3)
if farq > 1:
   print(f"Yer sayyorasining hajmi {farq} marta katta")
else:
   print(f"Yer sayyorasining hajmi {round((1 / farq), 3)} marta kichik")
