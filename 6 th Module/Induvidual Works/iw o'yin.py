pul = int(input("Boshlangich miqdorni kiriting: "))
jami = pul
while pul < 10000:
  a = int(input("Kubikda qanday raqam paydo bo'ldi: "))
  if a == 3:
    print("Siz hammasini yutkazdingiz!")
    jami -= pul
    print('Jami qolgan miqdor: ', jami)
    break
  jami += 500
  print("500 so'mni yutib oldingiz")
  print('Jami pul miqdori: ', jami)
  break
print("O'yin yakunlandi")