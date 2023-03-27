print('10-topshiriq. Nima uchun?')

# Nima qilish kerak?

# Siz eski do‘stingiz bilan uchrashdingiz, u ham dasturlashni o‘rganmoqda, lekin boshqa o‘quv muassasida. Qahva ichib o‘tirganda, beaql o‘qituvchi ularga shartli operatorlar va sikllardan foydalanmasdan turib, kiritilgan ikkita raqamdan eng kattasini aniqlaydigan dastur yozish vazifasini berganidan shikoyat qildi. Sizning o‘quv kursingizda buni talab qilishmaganidan xursand bo‘lib, baribir do‘stingizga yordam berishga qaror qilasiz. Uning uchun bu dasturni yozib bering.

# Misol:

# Birinchi raqamni kiriting: 10
# Ikkinchi raqamni kiriting: 5

# Eng katta raqam: 10

# Maslahatlar va tavsiyalar:
# Summaning ayirmasini va sonlarning ayirmalarini, ayirmaning yig‘indilarini va sonlarning yig‘indilarini ko‘rib chiqing.
a = int(input("Birinchi raqamni kiriting: "))
b = int(input("Ikkinchi raqamni kiriting: "))

print(f"Eng katta raqam {(a // b * a + b // a * b) // (a // b + b // a)}")