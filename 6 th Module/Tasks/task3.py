raqam = int(input("Raqamni kiriting: "))
raqamlar_soni = 0
if raqam == 0:
  print("Raqamlar soni: 1")
else:
  while raqam > 0:
    raqam % 10
    raqamlar_soni +=1
    raqam //=10
  print(f"Raqamlar soni: {raqamlar_soni}")
