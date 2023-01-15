raqam = int(input("raqamni kiriting: "))
jami = 0
while raqam != 0:
  oxirgi_raqam = raqam % 10
  print(oxirgi_raqam)
  if oxirgi_raqam == 5:
    print("Uzilish aniqlandi")
    break
  jami += oxirgi_raqam  
  raqam //= 10  
print("Jami", jami)
