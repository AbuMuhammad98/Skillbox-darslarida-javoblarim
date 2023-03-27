print("1-topshiriq. Raqamlar yig'indisi")

# Nima qilish kerak

# Bitta musbat butun N sonni oladigan va 1 dan N gacha bo‘lgan barcha sonlar yig‘indisini chop etadigan summa_n funksiyasini yozing.

# Dastur ishiga misol:
# Quyidagi raqamni kiriting: 5

# 1 dan 5 gacha bo'lgan sonlar yig'indisi 15 ekanligini bilaman
def summ_n(n):
  a = sum(range(1, n+1))
  return a
n = int(input("Raqamni kiriting: "))
print(f"1 dan {n} gacha raqamlar yig'indisi {summ_n(n)} ga teng")