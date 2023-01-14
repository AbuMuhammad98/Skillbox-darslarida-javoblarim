ish_xaqqi = int(input("Oylik maoshingiz qancha: "))
if ish_xaqqi >= 50000:
    soliq = 0.3 * (ish_xaqqi - 50000) + 0.2 * (50000 - 10000) + 0.13 * (10000)
    print(soliq)
elif ish_xaqqi >= 10000:
  soliq_1 = 0.2 * (ish_xaqqi - 10000) + 0.13 * (10000)
  print(soliq_1)
else:
  soliq_2 = 0.13 * (ish_xaqqi)
  print(soliq_2)
  