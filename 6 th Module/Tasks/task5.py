chipta = int(input("Chipta raqamini kiriting: "))
while chipta > 0:
  dastlabki_uchlik = chipta // 1000
  dastlabki_uchlik_yigindi = 0
  if dastlabki_uchlik > 0: 
    while dastlabki_uchlik != 0:
      raqam1 = dastlabki_uchlik % 10
      dastlabki_uchlik_yigindi += raqam1
      dastlabki_uchlik //= 10     
  oxirgi_uchlik = chipta % 1000
  oxirgi_uchlik_yigindi = 0
  if oxirgi_uchlik > 0:
    while oxirgi_uchlik != 0:
      raqam2 = oxirgi_uchlik % 10
      oxirgi_uchlik_yigindi += raqam2
      oxirgi_uchlik //= 10
  if dastlabki_uchlik == oxirgi_uchlik and dastlabki_uchlik_yigindi == oxirgi_uchlik_yigindi:
    print(f"{chipta} raqamli chipta omadli")
    break
  else:
    print(f"{chipta} raqamli chipta omadsiz ")
    break