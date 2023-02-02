pre_month = 0
months = 0
past = 0
for month in range(1, 11):
  now_month = int(input(f"{month}-oy ish xaqqini  kiriting: "))
  if now_month < pre_month:
    past += 1
  else:
    pre_month = now_month
    months += 1      
if past > 0:    
  print('Oylik barqaror emas')
else:
    print('Oylik ortib bormoqda')    

