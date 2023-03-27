def KattaSon(a, b):
  return (a // b * a + b // a * b) // (a // b + b // a)

a = int(input("a = "))
b = int(input("b = "))

maximum1 = KattaSon(a ,b)

c = int(input("c = "))
maximum2 = KattaSon(maximum1, c)

print(f"Max son: {maximum2}")