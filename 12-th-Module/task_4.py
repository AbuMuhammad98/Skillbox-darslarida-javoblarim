print('4-topshiriq. Teskari son')

# Nima qilish kerak

# Nol bilan tugaydigan raqamlar ketma-ketligini kiriting. Har bir raqamni argument sifatida qabul qiladigan, uni teskari o'zgartiradigan va ekranga chiqaradigan funksiyani amalga oshiring.

# Misol:
# Raqamni kiriting: 1234
# Teskari raqam: 4321

# Raqamni kiriting: 1000
# Teskari raqam: 0001

# Raqamni kiriting: 0
# Dastur yakunlandi!

# Qo’shimcha: boshida nollar mavjud bo’lgan raqamlarning chiqishiga erishing.
  
# Raqamni kiriting: 1230
# Teskari raqam: 321

# Biz olib tashlagan nollar yetakchi deb nomlanadi.
son = 0

def teskari_raqam(son):
  
  while True:
    teskari_s = 0
    son = int(input("Raqamni kiriting: "))
    while son > 0:
      digit = son % 10
      son //= 10
      teskari_s *= 10
      teskari_s += digit  
    print(f"Teskari son: {teskari_s}")

teskari_raqam(son)

