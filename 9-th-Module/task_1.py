print('1-topshiriq. Taqvim')

# Nima qilish kerak

# Biz smartfon uchun qulay taqvim ishlab chiqishda davom etamiz. Kabisa yilini aniqlash funktsiyasini qo'shdik, lekin yana ko'p turli xil oddiy narsalarni unutdik.
# Foydalanuvchidan haftaning kunini satr sifatida qabul qiladigan va uning raqamini ekranda ko'rsatadigan dastur yozing.

# Misol:
# Haftaning kunini kiriting: seshanba
# Hafta kuninig raqami: 2

# Maslahatlar va tavsiyalar
# Haftaning kunlarini ("dushanba", "seshanba", "chorshanba") ko'rsatish uchun for sikli va ro'yxat(list)/kortej(tuple) dan foydalanish tavsiya etiladi...)

days = {'dushanba':1, 'seshanba':2, 'chorshanba':3, 'payshanba':4, 'juma':5, 'shanba':6, 'yakshanba':7}
for key, value in days.items():
   
    key = input("Hafta kunini kiriting: ").lower()
    if key in days.keys():
       print(f"{key.title()} Haftaning {days[key]} chi kuni")

       break