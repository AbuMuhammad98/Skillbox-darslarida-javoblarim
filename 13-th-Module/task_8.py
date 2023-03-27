print('8-topshiriq. Qator yig`indisi')

# Nima qilish kerak?

# Foydalanuvchi "x" haqiqiy sonini va "precision" aniqlikni kiritadi. x soni berilgan qator yig’indisini precision aniqlikgacha hisoblaydigan dasturni yozing.

# P.S: Formulani ko'rish uchun veb-saytga qarang :)

# Darajaga oshirish amali va factorial funktsiyasidan foydalanish mumkin emas. 

# Misol:

def factorial_num(n):
  factorial = 1
  for num in range (1, n + 1):
    factorial *= num
  return factorial

def degree_num(x, n):
    count = 1
    for num in range (1, n + 1):
          count = count * x
    return count

precision = float(input("Aniqlik miqdori: "))
x = int(input("x =  "))
addMember = 1
result = 0

n = 0

while abs(addMember) > precision:
    addMember = degree_num(-1, n) * (degree_num(x, (2 * n)) / factorial_num((2 * n)))
    result += addMember
    n += 1
print(f"Qatorlar yig'indisi = {result}")