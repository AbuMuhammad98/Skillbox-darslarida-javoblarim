print('1-topshiriq. Informatika darsi 2')

# Nima qilish kerak?

# Oxirgi marta o‘qituvchi raqamlarni suzuvchi nuqta formatida chiqaradigan dasturni yozgan edi, lekin u bir muhim narsani hisobga olmaganini esladi: axir sonlar noldan boshlanishi mumkinku.
# Musbat x (x > 0) son berilgan. Sizning vazifangiz uni suzuvchi nuqta formatiga keltirish, ya’ni x = a * 10 ** b, bu yerda 1 ≤ a < 10. 

# E’tibor bering, x endi noldan katta, birdan emas. Kirish nazoratini ta’minlang.

# 1-misol:
# Sonni kiriting: 92345
# Suzuvchi nuqta formati: x = 9.2345 * 10 ** 4 

# 2-misol:
# Sonni kiriting: 0.0012
# Suzuvchi nuqta formati: x = 1.2 * 10 ** -3

number = float(input("Raqamni kiriting: "))
def suzuvchi_nuqta(number):
  eksp = 0
  if number < 1:
    while number < 1:  
      number *= 10
      eksp -= 1
  elif number >= 10:
    while number >= 10:  
      number /= 10
      eksp += 1
  return f"Suzuvchi nuqta formati: x= {number} * 10 ** {eksp}"  
  
print(f"Sonni kiriting: {number}")
print(suzuvchi_nuqta(number))

