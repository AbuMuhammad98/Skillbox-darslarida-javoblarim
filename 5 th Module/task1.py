hero_score = int(input("Tajriba balini kiriting: "))
if hero_score >= 5000:
  level = 4
  print ("Sizning bosqichingiz: ", level)
elif hero_score >= 2500:
  level = 3
  print("Sizning bosqicingiz: ", level)
elif hero_score >= 1000:
  level = 2
  print("Sizning bosqicingiz: ", level)
else:
  level = 1
  print("Sizning bosqichingiz: ", level)