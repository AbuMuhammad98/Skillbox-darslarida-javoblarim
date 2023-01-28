qoida_buzarlik = 0
for sektor in range(30, 36):
  odamlar = int(input(f"{sektor}-sektordagi dagi odamlar soni: "))
  if odamlar > 10:
    print("Qoidabuzarlik! Sektordagi odamlar soni keragidan koʼp! ")
    qoida_buzarlik += 1
  else:
    print("Hammasi joyida")
print(f"Qoida buzarliklar soni: {qoida_buzarlik} ta")  