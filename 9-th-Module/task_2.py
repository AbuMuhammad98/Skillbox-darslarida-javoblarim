print('2-topshiriq. Men yangi qaroqchiga aylandim!')

# Nima qilish kerak

# Qari kapitan jamoani to'ldirishi kerak. Ammo uning kemasiga faqat munosiblar qabul qilinadi! U 10 kishini tanladi va ulardan "Karamba" so'zini baqiradiganlar bortga chiqariladi.
# Foydalanuvchi 10 ta so'zni kiritadi. Ularning qanchasi "Karamba" so'ziga mos kelishini aniqlaydigan dastur yozing.
jamoa = 0
for i in range(10):
  javob = input("Javobni kiriting: ")
  if (javob == "Karamba") or (javob == 'karamba'):
    jamoa += 1
print(f"Jamoaga {jamoa} ta a'zo qabul qilindi")
