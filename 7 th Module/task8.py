raqamlar = []
raqamlar_soni = 0
for raqam in range(10, 100):
  if raqam % 3 == 0:
    raqamlar.append(raqam)
    raqamlar_soni += 1

print(f"Raqamlarining uch baravariga teng bo'lgan ikki xonali raqamlar soni: {raqamlar_soni} ta va ular quyidagi raqamlar: {raqamlar}")
