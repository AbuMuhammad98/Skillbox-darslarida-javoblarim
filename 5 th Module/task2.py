alif = int(input("Birinchi soni kiriting: "))
lom = int(input("Ikkinchi soni kiriting: "))
mim = int(input("Uchinchi soni kiriting: "))
#  1 - usul
# maximum = max(alif, lom, mim)
# print(maximum)
#  2 - usul
if (alif > lom) and (alif > mim):
   print(alif)
elif (lom > mim) and (lom > alif):
    print(lom)
else:
  print(mim)