print('4-topshiriq. Teatr')

# Nima qilish kerak

# Ochiq osmon ostidagi teatrni qurish rejalashtirilgan, ammo avval siz qancha qator bo'lishi, qatorlardagi o'rindiqlar soni qancha bo'lisi  va qatorlar orasidagi masofa qanday bo’lgani yaxshiroq bo'lishni baholashingiz kerak.

# Kirish uchun qatorlar soni, o'rindiqlar soni va qatorlar orasidagi bo'sh metrlar sonini oladigan, so'ngra teatrning taxminiy maketini ekranga chiqaradigan dasturni yozing.

# Sahna
# Qatorlar sonini kiriting: 5
# Qatordagi o'rindiqlar sonini kiriting: 7
# Qatorlar orasidagi bo'sh metrlar masofasini kiriting: 3
#
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======

# Maslahatlar va tavsiyalar
# Siz sintaktik shakar: qatorni raqamga ko'paytirish va birlashtirish (satrlarni birlashtirish)dan foydalanishingiz mumkin. Boshlash uchun bitta qatorni oling.

qator = int(input("Qatorlar sonini kiriting: "))
joy = int(input("Qatordagi o'rindiqlar sonini  kiriting: "))
masofa = int(input("Qatorlar orasidagi oraliq masofani kiriting: "))
for teatr in range(qator):
  print("=" * joy + ' ' + "*" *  masofa + ' ' + "=" * joy)
  