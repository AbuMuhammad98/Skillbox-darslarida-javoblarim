print('9-vazifa. 2-piramidka')

# Nima qilish kerak

# Piramida darajalari sonini kirishda qabul qiladigan va ularni toq raqamlar bilan to'ldirgan holda ekranda ko'rsatadigan dasturni yozing:

# Misol:
 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

size = int(input("Qatorni kiriting: "))
number = 1

for row in range(size):
  boshliqlar = size - row -1
  print("   " * boshliqlar, end = '')
  for col in range(row + 1):
    print(number, end = '    ')
    number += 2
  print()