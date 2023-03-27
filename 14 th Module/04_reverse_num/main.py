def teskari_raqam(son):
  teskari_s = 0
  while son > 0:
    digit = son % 10
    son //= 10
    teskari_s *= 10
    teskari_s += digit
  return teskari_s

def mantissa(num):
  mant = str()
  for x in str(num):
    if x == '.':
      return int(mant)
    else:
      mant += x

def tartib(num):
  tartib1 = str()
  for x in str(num):
    if x == '.':
      tartib1 = str()
    else:
      tartib1 += x
  return int(tartib1)

N = float(input("Birinchi sonni kiriting: "))
K = float(input("Ikkinchi sonni kiriting: "))
num1 = mantissa(N)
num2 = tartib(N)
num3 = mantissa(K)
num4 = tartib(K)
teskari1 = teskari_raqam(num1)
teskari2 = teskari_raqam(num2)
teskari3 = teskari_raqam(num3)
teskari4 = teskari_raqam(num4)
teskari_son1 = float(str(teskari1) + '.' + str(teskari2))
teskari_son2 = float(str(teskari3) + '.' + str(teskari4))
print(f"Birinchi son teskari: {teskari_son1}")
print(f"Ikkinch son teskari: {teskari_son2}")
print(f"Yig'indi: {teskari_son1 + teskari_son2}")


