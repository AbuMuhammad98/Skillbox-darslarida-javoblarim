a = int(input("Birinchi son: "))
b = int(input("Ikkinchi son: "))
c = int(input("Uchinchi son: "))
if (a == b) and (b == c):
  print(3)
elif a == b or b == c or a == c:
  print(2)
else:
  print(0)