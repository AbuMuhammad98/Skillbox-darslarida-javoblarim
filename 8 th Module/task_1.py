print('1-topshiriq. Kosmik oziq-ovqat')

# Nima qilish kerak

# Sizning kosmik kemangiz cho'l sayyorasida halokatga uchradi. Bu yerda oziq-ovqat o'smaydi, lekin siz kema qoldiqlardan 100 kilogrammlik grechka yormasi to'la sumkani  qutqardingiz. O'tgan tajribadan bilasizki, agar siz ozgina ovqatlansangiz, oyiga to'rt kilogramm grechka sarflaysiz.
# Grechka byudjetini taxmin qilish uchun, siz bir oy, ikki oy va hokazodan keyin qancha kilogramm grechka qolishi  kerakligi haqida ma'lumot beradigan dastur yozishga qaror qildingiz. For siklidan foydalaning.

month = 0
grechka_yormasi = 100
for grechka in range(grechka_yormasi - 4, -1, -4):
  month += 1
  print(f"{month} - oydan so'ng: {grechka} kg grechka qoldi")