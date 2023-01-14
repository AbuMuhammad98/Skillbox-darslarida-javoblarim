alif = int(input("Birinchi soni kiriting: "))
lom = int(input("Ikkinchi soni kiriting: "))
mim = int(input("Uchinchi soni kiriting: "))
#  1 - usul
maximum = max(alif, lom, mim)
print(maximum)
#  2 - usul
if alif > lom:
  alif = maximum
  # print(maximum)
elif alif < lom:
  lom = maximum
  # print(maximum)
else:
  mim > lom
  mim = maximum
print(maximum)