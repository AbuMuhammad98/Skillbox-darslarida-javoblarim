print('9-topshiriq. Tenglama')

# Nima qilish kerak?

# Haqiqiy a, b, c koeffisientlari berilgan, bunda a≠0. ax2+bx+c=0 kvadrat tenglamani yeching va uning barcha ildizlarini chiqaring.
# Agar tenglama ikkita ildizga ega bo‘lsa, ikkala ildizni o‘sish tartibida chiqaring; agar bitta ildiz bo‘lsa - bitta raqamni chiqaring, agar ildiz bo‘lmasa - hech narsani chiqarmang.
# x = -b+-sqrt(d)/2a

# d = b2 - 4ac
from math import sqrt as s
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = (b ** 2) - (4 * a * c)
if d > 0:  
  x_1 = ((-b) + s(d)) / (2 * a)
  x_2 = ((-b) - s(d)) / (2 * a)
  print(f"x1 = {x_1}    x2 = {x_2}")
elif d == 0:
  x = (-b) / (2 * a)
else:
  print("Tenglama ildizga ega emas")