son = int(input("Raqamni kiriting: "))
raqamlar_yigindisi = 0
qolgan_raqamlar_yigindisi = 0
for raqam in range(1, son+1):
  raqamlar_yigindisi += raqam
  if raqam != son:
    q_k = int(input("Qolgan kartochka raqamini kiriting: "))
  
    qolgan_raqamlar_yigindisi += q_k
  
yoqolgan_karta = raqamlar_yigindisi - qolgan_raqamlar_yigindisi
print(f"Yo'qolgan karta {yoqolgan_karta}")