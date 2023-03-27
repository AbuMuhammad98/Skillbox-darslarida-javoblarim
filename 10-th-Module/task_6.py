print("6-vazifa. Faktoriallar yig'indisi")

# Nima qilish kerak

# Foydalanuvchidan N sonini so‘ragan va 1 ning faktoriallari yig‘indisini topadigan dasturni tuzing!

# Foydalanuvchidan N sonini so‘raydigan va 1! + 2! + 3! + ... + N! faktoriallari yig‘indisini topadigan dasturni tuzing!
# 1. 2! = 2. 3! = 6. 4! = 24. 5! = 120. 6! = 720. 7! = 5040. 8! = 40320.
number = int(input("N raqamini kiriting: "))
multiple = 1
summ = 1
for num in range(2, number + 1):
  multiple *= num
  summ += multiple
  print(f"{num} sonining faktoriali {summ}")
print(f"2 dan {number} gacha bolgan faktorial sonlarning yig'indisi {summ} ga teng")