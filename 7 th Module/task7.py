a = int(input("1-raqamni kiriting: "))
b = int(input("2-raqamni kiriting: "))
raqamlar_yigindisi = 0
raqamlar_soni = 0
for raqam in range(a, b+1):
  if raqam % 3 == 0:
    raqamlar_yigindisi += raqam
    raqamlar_soni +=1
  
orta_arifmetik = raqamlar_yigindisi/raqamlar_soni
print(f"3 sonining ko'paytmasi bo'lgan [a; b] kesimidagi barcha raqamlarning arifmetik o'rtacha qiymati: {orta_arifmetik}")