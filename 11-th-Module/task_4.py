print('4-topshiriq. Birinchi raqam')

# Musbat haqiqiy son X berilgan. O‘nlik nuqtadan keyin uning birinchi
# sonini chiqaring. Bu masalani yechayotganda shartli qo‘llanma, 
# sikl yoki qatorlardan foydalanish  mumkin emas.
raqam = float(input("Raqamni kiriting: "))
son = round(raqam, 1)
print(int(10 * (son % int(son))))
