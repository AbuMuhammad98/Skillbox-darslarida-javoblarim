pre_month = 0
for month in range(1, 11):
  now_month = int(input(f"{month}-oy ish xaqqimi  kiriting: "))
  if now_month < pre_month:
    print('Oylik pastladi')
    break
  else:
    pre_month = now_month
    print('Oylik ortdi yoki tartibda ketmoqda')

