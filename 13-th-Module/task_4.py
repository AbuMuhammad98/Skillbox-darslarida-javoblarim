print('4-topshiriq. Informatika darsi 3')

# Nima qilish kerak?

# Nihoyat, o‘qituvchi bolalarga «suzuvchi nuqta» nima ekanligini tushuntirib bera oldi. Biroq, uning quvonchi uzoqqa cho‘zilmadi, chunki keyingi darsda u «eksponensial», «mantissa» va «tartib»  kabi dahshatli so‘zlarni tushuntirib berishi kerak. Yuqori sinf o‘quvchilari eksponenta bilan tanish bo‘lsalar-da, o‘qituvchi bu yerda hamma narsa aniq bo‘lishiga hali ham ishonchi komil emas. Shuning uchun yaqqolroq ko‘rinishi uchun u yana dastur yozdi.

#   Kiritish satri - bu sonning eksponensial shakli. Bu sonning alohida mantissasini va alohida tartibini ko‘rsatadigan dasturni yozing.
num = input("Eksponensial sonni kiriting: ")

def mantissa(num):
  mant = str()
  for x in num:
    if x == 'e':
      print(f"Mantissa: {mant}")
    else:
      mant += x

def tartib(num):
  tartib1 = str()
  for x in num:
    if x == 'e':
      tartib1 = str()
    else:
      tartib1 += x
  print(f"Tartib: {tartib1}")

mantissa(num)   
tartib(num)





  
# mantissa(num)

