manfiy_baho = 0
musbat_baho = 0
while True:
  baho = int(input("Ilovani baholang: "))
  if baho < 0:
    manfiy_baho += 1
  elif baho > 0:
    musbat_baho += 1
  else:
    break

print(f"Musbat baholar: {musbat_baho}")
print(f"Manfiy baholar: {manfiy_baho}")