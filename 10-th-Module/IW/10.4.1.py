people = int(input("Odamlar sonini kiriting: "))
for hour in range(people + 1):
  print(f"Odamlar soni: {people}")
  for num in range(hour, people + 1):
    print("Navbatdagi raqam: ", num)
  print()


print("Navbatdagi barchaga xizmatlar ko'rsatildi")