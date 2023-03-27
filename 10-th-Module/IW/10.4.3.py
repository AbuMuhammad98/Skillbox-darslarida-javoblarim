size = int(input("Raqamni kiriting: "))
for row in range(size):
  for col in range(row, size + 1):
    print(col, ' ', end = '')
  print()