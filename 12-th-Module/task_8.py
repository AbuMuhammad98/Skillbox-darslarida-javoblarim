print('8-topshiriq. Eng katta umumiy boʻluvchi')

# Nima qilish kerak

# Ikki sonning eng katta umumiy bo‘luvchisini hisoblaydigan funksiyani yozing.
x = int(input("x = "))
y = int(input("y = "))
def EKUB(x, y):
  while x > 0 and y > 0:
    if x > y:
      x %= y
    else:
      y %= x
  
  return   f"EKUB = {x + y}"

print(EKUB(x, y))