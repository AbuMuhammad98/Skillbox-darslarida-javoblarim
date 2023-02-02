print("4-topshiriq. Kesimdagi o'rtacha")

# Nima qilish kerak

# Klaviaturadan ikkita a, b va c raqamlarini o'qiydigan  va [a; b] kesimidgi barcha c numberining ko'paytmasi bo'lgan raqamlarning arifmetik o'rtacha qiymatini hisoblaydigan va konsolga chiqaradigan dastur yozing.

# Maslahatlar va tavsiyalar
# range(start, stop) funktsiyasi stop chegarasini o'z ichiga olmaydi, unga etib bermasdan to'xtaydi.

start = int(input("[a - b] kesma boshidagi raqamni kiriting: "))
stop = int(input("[a - b] kesma oxiridagi raqamni kiriting: "))
number_summ = 0
number_digits = 0
number = int(input("Karrali numberni kiriting: "))
for raqam in range(start, stop + 1):
  if raqam % number == 0:
    number_summ += raqam
    number_digits += 1
print(f"[a - b] kesmadagi raqamlarning yig'indisi: {number_summ} ga teng")
print(f"[a - b] kesmadagi {number} ga karrali raqamlar numberi: {number_digits}")
print(f"[a - b] kesmadagi raqamlarning o'rta arifmetik qiymati: {number_summ/number_digits} ga teng")
    