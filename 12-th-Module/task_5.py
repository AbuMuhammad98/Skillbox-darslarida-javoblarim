print('5-topshiriq. Matnli muharriri')

# Nima qilish kerak

# Biz yangi matnli muharrirni ishlab chiqishda davom etmoqdamiz va bu safar bizga u uchun matndagi istalgan harf va istalgan raqam (avvalgidek faqat Ы harfini emas) sonini hisoblaydigan kod yozish topshirildi.

# Kirishda matnni qabul qiladigan va undagi K raqamlar va N harflar sonini hisoblaydigan count_letter funksiyasini yozing. Funksiya topilgan harflar va raqamlar haqidagi ma'lumotlarni ma'lum formatda ekranda ko'rsatishi kerak.

# Misol:
# Matnni kiriting: tushlik vaqtida 100 yil
# Qaysi sonni qidiryapmiz? 0
# Qaysi harfni qidiryapmiz? l

# 0 raqami soni: 2
# l harfi soni: 2

def count_letter():
  text = input('Matnni kiriting: ')
  number = int(input('Qaysi sonni qidiryapsiz?: '))
  letter = input('Qaysi harfni qidiryapsiz?: ')
  number_count, letter_count = 0, 0

  for symbol in text:
    if symbol == letter:
      letter_count += 1
    elif symbol == str(number):
      number_count += 1
  print(f"{number} raqami: {number_count}")
  print(f"{letter} harfi: {letter_count}")

count_letter()