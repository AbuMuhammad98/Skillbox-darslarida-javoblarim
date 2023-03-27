print('6-topshiriq. Tangacha')

# Nima qilish kerak

# Amaliyotchiga berilgan koordinatalar asosida eski metall tangachani topish vazifasi berildi. Metall qidiruvchidan foydalanuvchi atrofidagi maydonni skanerlaydi va metall aniqlanganda/yo'q bo'lganda, qurilma ekranda tegishli xabarni ko'rsatadi.

# Ikkita haqiqiy x va y sonlari berilgan. Koordinatalari (x, y) bo'lgan nuqta shtrixlangan kvadratga (shu jumladan uning chegarasi) tegishli yoki yo'qligini tekshiradigan funksiyani yozing. Agar nuqta kvadratga tegishli bo'lsa, «Tangacha shu yaqinda» degan xabarni chiqaring, aks holda «Ushbu joyda tangacha yo'q» xabarini ko'rsating. Rasmda panjara qadam 1 bilan amalga oshirilgan.

# P.S - Saytdagi rasmga qarang :)
#         ^
#         |
#        *|*
# ========+=======>
#        *|*
#         |
x = int(input("x = "))
y = int(input("y = "))
step = 1
def money(x, y, step):
  return "Tangacha shu yaqinda" if abs(x) <= step and abs(y) <= step else "Ushbu joyda tangacha yo'q"

print(money(x, y, step))