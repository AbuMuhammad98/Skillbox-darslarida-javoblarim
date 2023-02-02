print("3-topshiriq. Bu bomba bo'ladi")

# Nima qilish kerak

# Biz jangari film asosida qadqm-baqadam  o'yinni ishlab chiqmoqdamiz. Markaziy personajning vazifasi  - N soniyadan keyin portlaydigan bombani zararsizlantirish. Dastur foydalanuvchidan hozirda bombani zararsizlantirishni xohlaysizmi, deb so'raydi.
# Agar javob 0  (ya'ni" yo'q") bo'lsa, unda bomba hisoblagichi kamayadi. Agar u nolga yetgan bo'lsa,  dastur "bomba portladi" degan xabarni beradi va agar u yetib bormagan bo'lsa, dastur yana o'yinchidan bombani zararsizlantirishni xohlaysizmi, deb so'raydi va portlashga qancha vaqt qolganligini aytadi. Agar javob " ha " bo'lsa, dastur ekranda bomba portlashdan 20 soniya oldin zararsizlantirilganligi haqidagi xabarni ko'rsatadi.

# Taymer nolga tushguncha vaqtni belgilang.
# ● for siklidan foydalaning.
# ● Har bir iteratsiyada  bombani zararsizlantirishni xohlaysizmi yoki o'yin atmosferasini kuchaytirishda davom etasizmi degan savolni bering.


timer = int(input("Bombaning portlash vaqti: "))

for time in range(timer, -1, -1):
  print(f"Bomba portlashiga qolgan vaqt: {time}")
  diler = int(input("Bombani zararsizlantirishni xoxlaysizmi yoki o'yin atmosferasini kuchaytirishda davom etasizmi: (1 - davom etish; 2 - to'xtatish): "))
  if time == 0:
    print("Bomba portladi")
  
    
  if diler != 2:
    time -=1
  else:
    print(f"Bomba portlashidan {time} soniya oldin zararsizlantirildi")
    break