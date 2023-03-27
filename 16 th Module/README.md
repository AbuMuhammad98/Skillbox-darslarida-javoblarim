## Merge requests haqida

Ushbu modulda Merge requests funksionalligi haqida so’z boradi va har bir vazifa uchun o'z GIT shoxchangizni yaratishingiz kerakligi aytiladi.
Biroq, vazifalar juda kichik (haqiqiy loyihalarga nisbatan) va ular bir-biriga bog'liq emasligi sababli, biz sizga **barcha vazifalarni bitta shoxchada** bajarishni taklif qilamiz.

Bitta shoxcha va merge request hosil bo’ladi.

Endi bu ishni osonlashtirishga imkon beradi, ammo kelajakda Python ning keyingi kurslarini o'tayotganda turli xil merge requests larni amalga oshirishga to’g’ri kelishi mumkin.
## Uyga vazifaning maqsadi
Pythonda axborot taqdim etishni ro‘yxat ko‘rinishida mustahkamlash va quyidagilarni amalga oshirish uchun yangi uslublardan foydalanishni o‘rganib olish:
- Ob’ektni ro‘yxatdagi muayyan joyga kiritish;
- Ro‘yxatdagi unsurning indeksini aniqlash;
- Unsurni ro‘yxatdan olib tashlash;
- Bir ro‘yxatni boshqasi bilan kengaytirish;
- Ro‘yxatdagi aniqlangan unsurlar sonini hisoblash.
- Ro‘yxatni yuzaga keltirish uchun list va range funksiyalaridan foydalanishni o‘rganib olish.
- Kiritilgan ro‘yxatlarning unsurlari bilan ishlash ko‘nikmasini shakllantirish.
## Topshiriqga nimalar kiradi?
- 1-topshiriq. Qo‘rqinchli kod.
- 2-topshiriq. Qator.
- 3-topshiriq. Detallar.
- 4-topshiriq. Bazm kechasi.
- 5-topshiriq. Qo‘shiqlar.
- 6-topshiriq. Noyob unsurlar.
- 7-topshiriq. Roliklar.
- 8-topshiriq. Sanoq.
- 9-topshiriq. Do‘stlar.
- 10-topshiriq. Simmetrik ketma-ketlik.
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
## 2-topshiriq. Qator
### Nima qilish kerak?
Ikkita sinf alohida qatorda saf tortib turibdi. Har bir sinfda o‘quvchilar bo‘y-bastiga qarab (o‘sib borish tartibida) safga qo‘yilgan: bir sinfda 160 smdan 176 smgacha, 2 qadam oraliq bilan, ikkinchi sinfda— 162 smdan 180 smgacha, 3 qadam oraliq bilan. Qandaydir vaqtdan so‘ng, ikkita sinfni bir qatorga birlashtirishadi va bunda ham ularni bo‘y-basti bo‘yicha o‘sib borish tartibida safga tizishadi.
Sinfdagi har bir o‘quvchi uchun bo‘y ro‘yxatini yuzaga keltiradigan, keyin ularni bir ro‘yxatga birlashtiradigan va o‘sib borish tartibida saralaydigan dastur yozing. Saralangan ro‘yxatni ekranga chiqaring.

Javobni chiqarish shakli:

O‘quvchilarning saralangan ro‘yxati: [160, 162, …]
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Chiqarib berish shakli vazifada ko‘rsatilganiga to‘g‘ri keladi.
- Saralash alohida funksiyada bayon qilingan.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).

## 3-topshiriq. Detallar
### Nima qilish kerak?
Mayda-chuydalar do‘konining ma’lumotlar bazasida detallar va ularning narxini o‘z ichiga olgan ro‘yxat saqlanmoqda:

```python
shop = [['siljima qism', 1200], ['shatun', 1000], ["o'rindiq", 300], ['tepki', 100], ["o'rindiq", 1500], ['rama', 12000], ['gardish', 2000], ['shatun', 200], ["o'rindiq", 2700]]
```

Sotuvchi detallarning soni va narxini qo‘l harakati bilan hisoblash noqulay degan qarorga keldi. Shuning uchun bu jarayonni maqbullashtirish maqsadida dasturchidan yordam so‘rashga qaror qildi.
Foydalanuvchidan detalning nomini so‘raydigan, ularning sonini, shuningdek, umumiy  narxini hisoblab chiqaradigan dastur yozing.
Misol:

```
Detalning nomi: o‘rindiq
Detallar soni — 3
Umumiy narxi — 4500
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).
## 4-topshiriq. Bazm kechasi
### Nima qilish kerak?
O‘zining tug‘ilgan kuni sharafiga Artyom o‘z dala hovlisida bazm kechasi uyushtirishga qaror qildi. U taklifnomalar jo‘natib o‘tirmadi, balki shunchaki hammaga xabar qildi: «Agar istasangiz — keling va o‘z do‘stlaringizni ham chaqiring». Bazm kechasi davomida odamlar kelishar va ketishardi, hamma ham tunab qolmadi. Buning ustiga dala hovlining o‘zi ham rezinadan qilinmagan — unga atigi olti kishi sig‘adi.
Mehmonlarning dastlabki ro‘yxati — boshida kelganlarning ismi berilgan:

```python
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
```

Foydalanuvchidan biror odam ketgani yoki yangi mehmon kelganini so‘raydigan va javobdan kelib chiqib, kerakli ismni ro‘yxatga kiritadigan yoki ro‘yxatdan o‘chiradigan dastur yozing. Bunda mehmonlar olti kishidan ko‘p bo‘lmasligi mumkin. Toki foydalanuvchi “Uxlash vaqti bo‘ldi” degan xabarni kiritmagunicha, ismlar so‘ralaveradi.
Misol:
```
Hozir bazm kechasida 5 kishi: [‘Petya’, ‘Vanya’, ‘Sasha’, ‘Liza’, ‘Katya’]
Mehmon keldimi yoki ketdimi? keldi
Mehmonning ismi: Aleks
Salom, Aleks!
 
Hozir bazm kechasida 6 kishi: [‘Petya’, ‘Vanya’, ‘Sasha’, ‘Liza’, ‘Katya’, ‘Aleks’]
Mehmon keldimi yoki ketdimi? keldi
Mehmonning ismi: Gosha
Uzr, Gosha, lekin joy yo‘q.
 
Hozir bazm kechasida 6 kishi: [‘Petya’, ‘Vanya’, ‘Sasha’, ‘Liza’, ‘Katya’, ‘Aleks’]
Mehmon keldimi yoki ketdmi? ketdi
Mehmonning ismi: Vanya
Xayr, Vanya!
 
Hozir bazm kechasida 5 kishi: [‘Petya’, ‘Sasha’, ‘Liza’, ‘Katya’, ‘Aleks’]
Mehmon keldimi yoki ketdmi? Uxlash vaqti bo‘ldi
 
Bazm kechasi tugadi, hamma uxlash uchun yotdi.
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).
## 5-topshiriq. Qo‘shiqlar
### Nima qilish kerak?
Biz qulay tarzda musiqa tinglash uchun ilova yozayapmiz. Vanyada Depeche Mode guruhining to‘qqizta qo‘shig‘idan iborat ro‘yxat bor. Ro‘yxat har bir qo‘shiq nomidan va daqiqaning ulushigacha aniqlikdagi davomiylikdan tashkil topgan:
```python
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
```

Vanya shu ro‘yxatdan N qo‘shiqni tanlab olishni va uni boshqa treklari bo‘lgan alohida pleylistga tashlab qo‘yishni istayapti. Bunda yig‘indida ushbu N qo‘shiqlar qancha vaqt eshitilib turishi ham unga muhimdir. 

Foydalanuvchidan ro‘yxatdagi qo‘shiqlar sonini va keyin shu qo‘shiqlarning nomini so‘raydigan, ekranga esa ular eshitilib turishining umumiy vaqtini chiqarib beradigan dastur yozing.
Misol:

```
Nechta qo‘shiqni tanlash lozim? 3 ta
1-qo‘shiqning nomiy: Halo
2-qo‘shiqning nomi: Enjoy the Silence
3-qo‘shiqning nomi: Clean
 
Qo‘shiqlar eshitilib turishining umumiy vaqti: 14,93 daqiqa
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).
## 6-topshiriq. Noyob unsurlar
### Nima qilish kerak?
Butun sonlarning ikkita ro‘yxati berilgan, ikkala ro‘yxat ham klaviatura orqali to‘ldiriladi. Birinchi ro‘yxatga  uchta son, ikkinchisiga - yettita son kiritiladi. Foydalanuvchidan bu sonlarni so‘raydigan, keyin birinchi ro‘yxatni ikkinchisining unsurlari bilan kengaytiradigan, shundan so‘ng birinchi ro‘yxatda faqat noyob unsurlarnigina qoldiradigan, ya’ni sonlarning ortiqcha takrorlanishini o‘chiradigan dastur yozing. Shartli operatordan foydalanish mumkin emas.
Misol:

```
Birinchi ro‘yxat uchun 1-sonni kiriting: 1
Birinchi ro‘yxat uchun 2-sonni kiriting: 2
Birinchi ro‘yxat uchun 3-sonni kiriting: 3
Ikkinchi ro‘yxat uchun 1-sonni kiriting: 2
Ikkinchi ro‘yxat uchun 2-sonni kiriting: 4
Ikkinchi ro‘yxat uchun 3-sonni kiriting: 6
Ikkinchi ro‘yxat uchun 4-sonni kiriting: 3
Ikkinchi ro‘yxat uchun 5-sonni kiriting: 3
Ikkinchi ro‘yxat uchun 6-sonni kiriting: 2
Ikkinchi ro‘yxat uchun 7-sonni kiriting: 1
 
Birinchi ro‘yxat: [1, 2, 3]
Ikkinchi ro‘yxat: [2, 4, 6, 3, 3, 2, 1]
 
Noyob unsurlarga ega yangi birinchi ro‘yxat: [4, 6, 3, 2, 1]
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- Vazifani bajarish uchun setdan foydalanilmayapti.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).
## 7-topshiriq. Roliklar
### Nima qilish kerak?
Xususiy idora turli o‘lchamdagi roliklarni ijaraga beradi. Odam o‘zining oyog‘i o‘lchamidan kam bo‘lmagan har qanday rolikni kiyishi mumkin.

Foydalanuvchi o‘lchamlarning ikkita ro‘yxatini kiritadi: konkilarning N o‘lchamlari va odamlar oyog‘ining K o‘lchamlari ro‘yxati. Bir vaqtning o‘zida qancha ko‘p odam roliklarni olishi va konkida uchishga borishini aniqlab beradigan kodni amalga oshiring. 
Misol:

```
Konkilar soni: 4 ta
1-juftning o‘lchami: 41
2-juftning o‘lchami: 40
3-juftning o‘lchami: 39
4-juftning o‘lchami: 42
 
Odamlar soni: 3 nafar
1-odam oyog‘ining o‘lchami: 42
2-odam oyog‘ining o‘lchami: 41
3-odam oyog‘ining o‘lchami: 42
 
Roliklarni olishi mumkin bo‘lgan eng ko‘p odamlar: 2 nafar
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).
## 8-topshiriq. Sanoq
### Nima qilish kerak?
1 dan Ngacha sonlar bilan raqamlangan N odamlar doira bo‘lib turishibdi. Ular chiqib ketish sharti bilan sanoq o‘yinini boshlashadi, bu yerda sanoq bo‘yicha har bir K odam doiradan chiqib ketadi, shundan so‘ng sanoq chiqib ketgan odamdan keyingi kishidan boshlab davom etadi.

Kiritishga odamlarning N miqdori va K raqam beriladi. 1 dan Ngacha sonni - bu doirada oxirgi bo‘lib qoladigan odamning raqamini chiqarib beradigan dastur yozing.
Misol:

```
Odamlar soni: 5 nafar
Sanoqdagi qaysi son? 7
Demak, har 7-kishi chiqib ketadi
 
Odamlarning joriy doirasi: [1, 2, 3, 4, 5]
Sanoq 1 raqamidan boshlanadi
2-raqamli odam chiqib ketadi
 
Odamlarning joriy doirasi: [1, 3, 4, 5]
Sanoq 3 raqamidan boshlanadi
5-raqamli odam chiqib ketadi
 
Odamlarning joriy doirasi: [1, 3, 4]
Sanoq 1 raqamidan boshlanadi
1-raqamli odam chiqib ketadi
 
Odamlarning joriy doiraasi: [3, 4]
Sanoq 3 raqamidan boshlanadi
3-raqamli odam chiqib ketadi
 
4-raqamli odam qoldi
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).
## 9-topshiriq. Do‘stlar
### Nima qilish kerak?
N do‘stlar har doim bir-biridan qarz olib turishadi. Qandaydir bir paytda kim kimga qancha qarz ekanligini esdan chiqarib qo‘yaverish ularning joniga tegdi va ular qarz tilxatlari tizimini o‘ylab topishdi. Yangi yilni “toza varaqdan boshlash” uchun, do‘stlar bir-birlariga nisbatan to‘planib qolgan barcha qarz tilxatlarini to‘lashga qaror qilishdi. Biroq ayni bir kishi har xil kunlarda ham qazrdor, ham qarz beruvchi rolida bo‘lganligi aniqlandi.

Berilgan tilxatlar bo‘yicha har bir do‘st boshqasiga qancha qarz to‘lashini (yoki boshqasidan qancha olish zarurligini) hisoblab chiqaradigan dastur yozing.

Avvaliga N soni kiritiladi — bu do‘stlar soni, keyin K soni kiritiladi— bu qarz tilxatlarining soni, shundan so‘ng sonlarning K uchligi keladi: qarz olgan do‘stning raqami, pul bergan do‘stning raqami va summa. Do‘stlardan hech biri o‘zi o‘zidan qarz olmaganligi kafolatlanadi.

Dastur “do‘stlar balansi”ni, ya’ni do‘stlar olishi yoki berishi kerak bo‘lgan summalarni chiqarib berishi kerak. Musbat sonlar do‘st boshqalardan pul olishi zarurligini bildiradi.

1-misol:

```
Do‘stlar miqdori: 2 nafar
Qarz tilxatlari: 3 ta
 
1- tilxat
Kimga: 1
Kimdan: 2
Qancha: 10
 
2-tilxat
Kimga: 1
Kimdan: 2
Qancha: 20
 
3-tilxat
Kimga: 1
Kimdan: 2
Qancha: 20
 
Do‘stlar balansi:
1: -50
2: 50
```

2-misol:

```
Do‘stlar soni: 3 nafar
Qarz tilxatlari: 1 ta
 
1-tilxat
Kimga 3
Kimdan: 1
Qancha: 100
 
Do‘stlar balansi:
1 : 100
2 : 0
3 : -100
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).

## 10-topshiriq. Simmetrik ketma-ketlik
### Nima qilish kerak?
Agar sonlarning ketma-ketligi chapdan o‘ngga ham, o‘ngdan chapga ham bir xilda o‘qilsa, bu simmetrik ketma-ketlik deb ataladi. Misol uchun, quyidagi ketma-ketliklar simmetrik hisoblanadi:
```
1 2 3 4 5 4 3 2 1
1 2 1 2 2 1 2 1
```

Foydalanuvchi N sonlardan iborat ketma-ketlikni kiritadi. Ketma-ketlik simmetrik bo‘lishi uchun bu ketma-ketlikning oxiriga qaysi eng kichik sonni va qaysi sonlarni qo‘shib qo‘yish zarurligini aniqlovchi dastur yozing.
1-misol:

```
Sonlar miqdori: 5
Son: 1
Son: 2
Son: 1
Son: 2
Son: 2
 
Ketma-ketlik: [1, 2, 1, 2, 2]
Sonlarni qo‘shib qo‘yish kerak: 3
Sonlarning o‘zi: [1, 2, 1]
```

2-misol:

```
Sonlar miqdori: 5
Son: 1
Son: 2
Son: 3
Son: 4
Son: 5
 
Ketma-ketlik: [1, 2, 3, 4, 5]
Sonlarni qo‘shish kerak: 4 ta
Sonlarning o‘zi: [4, 3, 2, 1]
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).

## Uyga vazifada nima baholanadi?
- Uyga vazifa GitLab orqali topshirilgan.
- Jildlar va repozitoriy fayllarining tuzilishi python_basic_uz repozitoriyiga mos keladi.
- Hamma vazifalar `main.py`ning tegishli jildlari va fayllarida bajarilgan.
- Kommitlarning bayoni anglangan va tushunarli: `111`, `done`, `men qildim` — noto‘g‘ri, `added m15 homework`, `14.3 fix: variables naming` — to‘g‘ri.
- Shunchaki `i` bo‘lmagan, nomlangan indekslar ishlatilgan (batafsil 7.2-videoda).
- Foydalanuvchi tomonidan qo‘shimcha harakatlarsiz, `+1` siz to‘g‘ri sonlar ishlatilgan (bu haqda batafsil 7.4-videoda).
- Kiritish uchun quruq salomlashishsiz, `input` to‘g‘ri rasmiylashtirilgan (bu haqda batafsil 2.3-videoda).
- O‘zgaruvchilar faqat `a`, `b`, `c`, `d` bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).
- Vergullardan so‘ng va binar operatsiyalarda bo‘shliqlar (probellar) mavjud.
- Funksiyalarning nomlari va qavslardan keyin bo‘shliqlar yo‘q: `print ()`, `input ()` — noto‘g‘ri, `print()` — to‘g‘ri.
- `if-elif-else` bloklari, sikllar va funksiyalar to‘g‘ri rasmiylashtirilgan, bir darajadagi barcha bloklarda xatboshi bir xil.

## Maslahatlar va tavsiyalar
- [PEP8](https://docs.python.org/3.7/reference/expressions.html#operator-precedence) arifmetik operatsiyalari ustuvorlikda qolmoqda. and, orni kiritish zarur.
- Python [PEP8](https://www.python.org/dev/peps/pep-0008/) uslubi bo‘yicha qo‘llanma ingliz tilida.
- Python [PEP8](https://pep8.ru/doc/pep8/) uslubi bo‘yicha qo‘llaanma uz tilida.
- [Kiritilgan funksiyalar ro‘yxati.](https://docs.python.org/3.7/library/functions.html).

## Topshiriqlarni qanday qilib tekshirishga jo‘natish lozim?
Amaliy mashg‘ulotni bajarish uchun, python_basic_uz repozitoriysini IDE PyCharm yordamida o‘z kompyuteringizga ko‘chiring. Vazifalar Module16 jildida joylashgan.

Bu modulning uy ishini Skillbox Gitlab servisidagi Git versiyalarni nazorat qilish tizimi orqali topshiring. Uyga vazifa darsda “Bajarildi” deb yozing va repozitoriyga havolani biriktiring. Replitga havolalar qoldirish shart emas.
