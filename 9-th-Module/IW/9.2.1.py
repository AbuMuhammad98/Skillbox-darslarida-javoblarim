bad_grade = 0
for talaba in range(5):
  javob = input("'Evgeniy Onegin' asari muallifi kim? ").title()
  if javob == 'Pushkin':
    print("Javob to'g'ri. ")
    break
  else:
    print("Javob noto'g'ri. Baho 2")
    bad_grade += 1

print("Yomon baho olgan talabalar")