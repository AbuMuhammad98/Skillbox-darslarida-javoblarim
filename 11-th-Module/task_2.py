print("2-topshiriq. Qo'pol matematika")

# Nima qilish kerak?

# Turli matematik tahlil bilan shug‘ullanadigan bir tahliliy markazda ba’zi bir funksiyalarni hisoblash uchun dastur yozgan amaliyotchi bor edi. To‘g‘ri, o‘sha kuni u juda charchagan va texnik topshiriqni biroz noto‘g‘ri o‘qigan va funksiyalar endi juda qo‘pol hisoblanayapti.
# N ta moddiy sonlar ketma-ketligi kiritiladi. Musbat sonlar yuqoriga qarab yaxlitlanadi, manfiy sonlar esa pastga qarab yaxlitlanadi. Agar son musbat bo‘lsa, uning natural logarifmini, manfiy bo‘lsa, sonning darajasiga eksponentasini chiqaradigan dastur tuzing.

# Misol:

# Sonlar miqdorini kiriting: 3
# Sonni kiriting: 1.3
# x = 2   log(x) = 0.6931471805599453 
# Sonni kiriting: -2.1
# x = -3   exp(x) = 0.049787068367863944 
# Sonni kiriting: -5.9
# x = -6   exp(x) = 0.0024787521766663585
import math as m
m_sonlar = int(input("sonlar ketma-ketligini kiriting: "))
for sonlar in range(1, m_sonlar + 1):
    raqam = float(input(f"{sonlar}-sonni kiriting: "))
    if raqam >0:
      shift = m.ceil(raqam)
    else:
      pol = m.floor(raqam)
    if raqam > 0:
      log_n = m.log(shift)
      print(f"x = {shift}  log(x) = {log_n}")
    else:
      eksponenta = m.exp(pol)
      print(f"x = {pol}  exp(x) = {eksponenta}")