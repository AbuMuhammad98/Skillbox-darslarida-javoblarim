raqam = int(input("Biror bir raqamni o'ylang: "))
print(f"Men bir raqamni o'yladim.")
taxminlar_soni = 0
while True:
  taxmin = int(input("Raqamni kiriting: "))
  taxminlar_soni += 1
  if taxmin < raqam:
    print("Raqam kerak bo'lganidan kamroq. Yana bir bor urinib ko`ring!")
  elif taxmin > raqam:
    print("Raqam kerak bo'lganidan ko'proq. Yana bir bor urinib ko`ring!")
  else:
    print(f"Siz topdingiz! Urinishlar soni:   {taxminlar_soni}")
    break