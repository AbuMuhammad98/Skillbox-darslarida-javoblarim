print('10-topshiriq. Buterbrod usuli')

# Nima qilish kerak

# "Super-Secret-no" maxfiy agentligi o'z xodimlarining yozishmalarini shifrlash uchun"buterbrod usuli" dan foydalanishga qaror qildi. Avval, so'zning harflari quyidagi tartibda raqamlanadi: birinchi harf 1 raqamini, oxirgi harf 2 raqamini, ikkinchisi 3 raqamini, oxirgi harf 4 raqamini, keyin uchinchi... va hokazo barcha harflar uchun (rasmga qarang). Keyin barcha harflar ularning raqamlari tartibida shifrga yoziladi..

# Masalan,   «sandwich» so’zi «shacnidw» ga shifrlanadi.

# Afsuski, "Super-Secret-no" dasturchisi faqat shifrlash dasturini yozdi va ishdan ketdi. Endi agentlar bir-birlariga nima yozganlarini tushunolmayaptilar. Ularga kiritilgan xabarlarning shifrini ochadigan dekoder dasturini yozishga yordam bering.
  
# Misol:
# Shifrlangan xabarni kiriting: shacnidw
# Shifrsizlangan xabar: sandwich
#           1   3   5   7   8   6   4   2
# So'z:  | s | a | n | d | w | i | c | h |
#
# Shifr: | s | h | a | c | n | i | d | w |


dekoder = []
shifr = input("Shifrlangan xabarni kiriting: ")
for kod in shifr:
  dekoder += kod
  a = dekoder[0] + dekoder[2] + dekoder[4] + dekoder[6] + dekoder[7] + dekoder[5] + dekoder[3] + dekoder[1]
print(a)


shifr = input("Shifrlangan xabarni kiriting: ")
harf1 = ''
harf2 = ''
harflar_soni = 0
for kod in shifr:
  print(kod)
  harflar_soni += 1
  if (harflar_soni % 2) == 1:
    harf1 += kod
  else:
    harf2 = kod + harf2
print(harf1 + harf2)