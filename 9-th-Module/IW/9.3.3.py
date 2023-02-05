katta_harf = 0
kichik_harf = 0
matn = input("Matnni kiriting: ")
for symbol in matn:
  if symbol == 'A':
    katta_harf += 1
  elif symbol == 'a':
    kichik_harf += 1

print(f"Katta A harflar soni: {katta_harf} \nKichik a harflar soni: {kichik_harf}")
