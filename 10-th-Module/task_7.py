print("7-vazifa. Raqamlarning eng katta yig'indisi")

# Nima qilish kerak

# Foydalanuvchi N raqamni kiritadi. Kiritilgan natural sonlar orasidan raqamlar yig‘indisi bo‘yicha eng kattasini toping. Ushbu raqamni va uning raqamlari yig'indisini ekranda namoyish eting.
raqamlar_soni = int(input("Raqamlar sonini kiriting: "))
raqamlar = []
raq_yig = 0
jami = 0
raqamlar1 = []
raqamlar2 = []
for i in range(1, raqamlar_soni + 1):
  print(f"{i}-raqamni")
  raqam = int(input("kiriting: "))
  raqamlar1.append(raqam)
  for son in str(raqam):
    raq_yig += int(son)  
  raqamlar.append(raq_yig)
  if raq_yig > jami:
      jami = raq_yig
  raq_yig = 0
maximum = max(raqamlar)
raq_yig2 = 0
for j in raqamlar1:
  for k in str(j):
    raq_yig2 += int(k)
  if raq_yig2 == maximum:
      raqamlar2.append(j)
      
    
  raq_yig2 = 0
maximum2 = max(raqamlar2)
print(f"Ro'yxatdagi raqamlar yig'indisi bo'yicha eng katta son: {maximum2}")
print(f"Uning raqamlar yig'indisi: {maximum} ga teng")  
