print('6-topshiriq. Mayatnik')

# Nima qilish kerak?

# Ma’lumki, tebranish mayatnigining amplitudasi har safar oldingi tebranish amplitudasining 8,4% ga pasayadi. Agar mayatnik silkitilsa, gapning ochig’i u hech qachon to‘xtamaydi, shunchaki amplituda doimiy ravishda pasayib boradi, toki biz bunday mayatnikni to‘xtagan deb hisoblamagunimizcha. Mayatnik to‘xtadi deb o‘ylashimizdan oldin uning necha marta tebranishini aniqlaydigan dastur yozing.

# Kirishda dastur tebranishning boshlang’ich amplitudasini santimetrlarda va mayatnikning to‘xtashi hisoblangan tebranishlarning oxirgi amplitudasini qabul qiladi. 
# Kirish nazoratini ta’minlang. 

# Misol:
  
# Boshlang’ish amplitudani kiriting: 1 
# To‘xtash amplitudasini kiriting: 0.1
  
# Mayatnik 27 ta tebranishdan keyin to‘xtagan deb hisoblanadi
a = float(input("Boshlang'ich amplitudani kiriting: "))
b = float(input("To'xtash amplitudasini kiriting: "))
def mayatnik(a, b):
  tebranish = 0
  while a > b:
    a -= a*0.084
    tebranish += 1
    if a == b:
      break
    
  print(f"Mayatnikning tebranishlar soni: {tebranish}")

mayatnik(a, b)