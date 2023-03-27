print('5-vazifa. Oddiy raqamlar')

# Nima qilish kerak

# Berilgan ketma-ketlikdagi oddiy raqamlarning sonini hisoblaydigan va javobni ekranga chiqaradigan dasturni tuzing.

# Misol:

# Raqamni kiriting: 6
# Raqamni kiriting: 4
# Raqamni kiriting: 7
# Raqamni kiriting: 20
# Raqamni kiriting: 3
# Raqamni kiriting: 11
# Raqamni kiriting: 37
# Ketma-ketlikdagi oddiy raqamlar soni: 4

# Maslahatlar va tavsiyalar
# Oddiy raqam - bu tabiiy (musbat butun son) raqam bo'lib, uning ikkita har xil tabiiy bo'luvchisi bor - bir va uning o'zi.
from math import sqrt
seq_num = int(input("Ketma-ketlikda nechta raqam bor: "))
numeral_count = 0
i = 2

for num in range(seq_num):
  
  print(f"{num+1} -  raqamni")
  number = int(input("kiriting: "))
  for k in range(i, int(sqrt(number)+1)):
    
      if number % k == 0:
        print(number, 'tub emas')
        break

    
        
  else:
        numeral_count += 1 
print(f"Ushbu sonlar ichida tub sonlar soni: {numeral_count} ta.")
