jami = 0
oy = 1
for oylar in range(1, 13):
  ish_xaqqi = int(input(f"{oy} - oy ish xaqqini kiriting: "))
  jami += ish_xaqqi
  oy +=1
print(f"O'rtacha oylik yaxlitlanganda {jami//12} ming so'mni tashkil etadi")
    