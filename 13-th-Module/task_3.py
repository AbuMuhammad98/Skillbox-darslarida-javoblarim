print('3-topshiriq. Teskari son 2')

# Nima qilish kerak?

# Foydalanuvchi ikkita - N va K sonni kiritadi. Har bir sonni raqamlarini teskari tartibda yozib, boshlang’ich sondan hosil bo‘ladigan, so‘ng ularni qo‘shib, yana teskari o‘giradigan va javobni ekranda ko‘rsatadigan dasturni yozing.
  
# Misol:

# Birinchi sonni kiriting: 102 
# Ikkinchi sonni kiriting: 123

# Birinchi songa teskari son: 201 
# Ikkinchi songa teskari son: 321 

# Yig’indi: 522
# Yig’indiga teskari son: 225
number1 = int(input("Birinchi sonni kiriting: "))
number2 = int(input("Ikkinchi sonni kiriting: "))
print()
def teskari_raqam(son):
  teskari_s = 0
  while son > 0:
    digit = son % 10
    son //= 10
    teskari_s *= 10
    teskari_s += digit  
  return teskari_s

number1_t = teskari_raqam(number1)
number2_t = teskari_raqam(number2)
print("Birinchi songa teskari son: ", number1_t)
print("Ikkinchi songa teskari son: ", number2_t)
print()
print("Yig'indi: ", number1_t + number2_t)
print("Yig'indiga teskari son: ", teskari_raqam(number1_t + number2_t))