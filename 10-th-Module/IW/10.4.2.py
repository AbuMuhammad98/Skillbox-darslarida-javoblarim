seq_num = int(input("Ketma-ketlikda nechta raqam bor: "))
numeral = int(input("Qaysi raqamni hisoblash kerak: "))
while (numeral < 0) or (numeral > 9):
  numeral = int(input("Hioblanadigan raqam 0 va 9 oraqlig'idagi raqamlardan iborat bo'lishi kerak, qayta kiriting: "))
numeral_summ = 0
for num in range(seq_num):
  print(f"{num} -  raqamni")
  number = int(input("kiriting: "))
  while number > 0: 
    if number % 10 == numeral:
       numeral_summ += numeral 
    number //= 10
    

print(f"Ushbu sonlar ichida {numeral} dan katta sonlar yigindisi: {numeral_summ}")