## 1-topshiriq. Qo‘rqinchli kod
### Nima qilish kerak?
Sizning Pythonni o‘rgana boshlagan do‘stingizga o‘qituvchi mana bunday vazifa berdi: uchta ro‘yxat bor — asosiy ro‘yxat va ikkita yordamchi ro‘yxat. Asosiy ro‘yxatda [1, 5, 3] unsurlar, yordamchi ro‘yxatlarda esa —  tegishlicha [1, 5, 1, 5] va [1, 3, 1, 5, 3, 3] unsurlar mavjud.

Birinchi yordamchi ro‘yxat asosiy ro‘yxatga tashlab qo‘yiladi, u yerda 5 raqamlarining miqdori hisoblanadi, miqdor ekranga chiqariladi keyin esa ular asosiy ro‘yxatdan o‘chiriladi. Shundan so‘ng, asosiy ro‘yxatga ikkinchi yordamchi ro‘yxat tashlab qo‘yiladi, u yerda 3 raqamlarining miqdori hisoblanadi va ekranga chiqariladi. Oxirida ro‘yxatning o‘zi ham chiqariladi.

Qiziqishdan kelib chiqib, siz do‘stingizdan uning dasturining kodini ko‘rsatishni so‘radingiz va buni bekorga qilmaganingizni tushundingiz — ko‘rgan narsangiz sizni lol qoldirdi va qo‘rquvga soldi. Mana kodning o‘zi:

```python
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
for i in b:
    a.append(i)
t = 0
for i in a:
    if i == 5:
        t += 1
print(t)
d = []
for i in a:
    if i != 5:
        d.append(i)
for i in c:
    d.append(i)
t = 0
for i in d:
    if i == 3:
        t += 1
print(t)
print(d)
```
Ro‘yxatlar uslubi haqidagi, shuningdek, dasturlash usuli haqidagi bilimlaringizdan foydalanib, do‘stingizga dasturni qaytadan yozishda yordam berasiz. Qo‘shimcha ro‘yxatlardan foydalanmang.

```
Dastur ishining natijasi:
Birinchi birlashishda 5 raqamlarining miqdori: 3
Ikkinchi birlashishda 3 raqamlarining miqdori: 4
Yakuniy ro‘yxat: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]
```

### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).