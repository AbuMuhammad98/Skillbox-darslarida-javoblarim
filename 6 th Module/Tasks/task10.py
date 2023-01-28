raqam = int(input("1 dan 100 gacha bo'lgan raqamnni o'ylang: "))
boshi_chegara = 1
oxirgi_chegara = 101
urinishlar_soni = 0
while True:
  taxmin = (boshi_chegara + oxirgi_chegara) // 2
  print(taxmin)
  javob = int(input( f"Sizning raqamingiz {taxmin} soniga tengmi, kichikmi yoki undan kattami?:(1 - teng; 2 - kichik; 3 - katta)"))
  urinishlar_soni +=1 
  if javob == 1:
    print(f"Ura topdim. {taxmin} sonini o'ylagan edingiz")
    break
  elif javob == 2:
    oxirgi_chegara = taxmin
  elif javob == 3:
    boshi_chegara = taxmin
   
print(f"Urinishlar soni esa {urinishlar_soni} ga teng")
    