student = int(input("O'quvchilar soni: "))
alochi = 0
yaxshi = 0
uch_baho = 0
for baholar in range(1, student+1):
  baho = int(input(f"{baholar}-o'quvchiga qo'yilgan baho: "))
  if baho == 5:
    alochi +=1
  elif baho == 4:
    yaxshi += 1
  else:
    uch_baho += 1
if alochi > yaxshi:
  print(f"Bugun 5 baho olgan o'quvchilar soni: {alochi} ta va ular sinfda eng ko'pini tashkil qiladi")
elif alochi < uch_baho:
  print(f"Bugun 3 baho olgan o'quvchilar soni: {uch_baho} ta va ular sinfda eng ko'pini tashkil qiladi")
else:
  print(f"Bugun 4 baho olgan o'quvchilar soni: {yaxshi} ta va ular sinfda eng ko'pini tashkil qiladi")