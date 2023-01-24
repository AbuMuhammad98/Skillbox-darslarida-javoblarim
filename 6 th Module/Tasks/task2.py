ism = input("Ismingiz nima: ")
qarz = int(input("Qarzingiz miqdorini kiriting: "))
qarz_berish = 0
print(f"{ism} sizning {qarz} qarzingiz bor")
while qarz_berish <=qarz:
  sorash=int(input("Buni to’lash uchun siz hozir qancha so'm kiritasiz? "))
  qarz_berish += sorash
  if qarz_berish >= qarz:
    print(f"Juda yaxshi, {ism}! Siz qarzingizni to'ladingiz. Rahmat")
    break
  else:
    print(f"Bu yetarli emas {ism}, yana to'lov qilishingiz kerak ")

   
     

  