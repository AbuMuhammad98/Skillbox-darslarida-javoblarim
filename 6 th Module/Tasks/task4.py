count = 0
while True:
  number = int(input("Kunlarni kiriting: "))
  count += (number % 2 == 0 and number != 0)
  if number == 0: 
    break
print(count)