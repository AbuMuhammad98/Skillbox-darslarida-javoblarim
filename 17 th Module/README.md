## Uyga vazifaning maqsadlari
Quyidagilarni uddalash:

- list comprehensions va undan foydalanishning afzalliklarini ta’riflash;
- ro‘yxatlarni yaratish uchun list comprehensions ishlatish (shartli mantiq bilan va shartli mantiqsiz);
- ro‘yxatlar kesmalarini nusxa yaratish, ro‘yxatning bir qismini olish va ro‘yxat ichidagi obyektlarni o‘zgartirish uchun ishlatish;
- masalalarni yechish uchun satrlarning indekslari va kesmalari bilan ishlash.
## Topshiriqga nimalar kiradi?
- 1-topshiriq. Unli harflar.
- 2-topshiriq. Yaratish.
- 3-topshiriq. Tasodifiy musobaqalar.
- 4-topshiriq. Kesmalar bilan mashq qilamiz.
- 5-topshiriq. Burilish.
- 6-topshiriq. Ro‘yxatni siqish.
- 7-topshiriq. Ikki o‘lchamli ro‘yxat.
- 8-topshiriq. O‘yin-kulgi.
- 9-topshiriq. Ro‘yxatlar ro‘yxati.
- 10-topshiriq. Sezar shifri.

Barcha masalalarda ro‘yxatlarni yaratish uchun list comprehensions ishlating.

## 1-topshiriq. Unli harflar
### Nima qilish kerak?
Tilshunoslar jamoasiga dasturlaringizning sifati yoqdi va ular Sizga matn tahlilchisi uchun matnning unli harflari ro‘yxatini tuzib, shu bilan birga ularning sonini ham hisoblaydigan funksiyaga buyurtma berishga qaror qilishdi.

Foydalanuvchiga matnga so‘rov beradigan va bu matnning unli harflari ro‘yxatini yaratadigan dasturni yozing (satrning o‘zi rus tilida kiritiladi). Konsolga ro‘yxatning o‘zi va uning uzunligini chiqaring.

Misol:

```
Matnni kiriting: Нужно отнести кольцо в Мордор!

Unli harflar ro‘yxati: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
Ro‘yxat uzunligi: 9
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).

## 2-topshiriq. Yaratish
### Nima qilish kerak?
Foydalanuvchi N butun sonini kiritadi. N sonlardan ro‘yxat yaratadigan dasturni yozing, undagi juft o‘rinlarda bir sonlari, toq o‘rinlarda esa — o‘z sonini 5 ga bo‘lgandagi qoldiqqa teng bo‘lgan sonlar turadi.

Misol:

```
Ro‘yxat uzunligini kiriting: 10
Natija: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli vazifada ko‘rsatilganiga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).

## 3-topshiriq. Tasodifiy musobaqalar
### Nima qilish kerak?
Biz ba’zi bir musobaqalarning ishtirokchilari uchun elektron jadvalning ishlashini sinab ko‘rmoqchimiz. Har birida 20 ta ishtirokchi bo‘lgan ikkita ro‘yxat (ya’ni ikkita jamoa) mavjud. Bu ro‘yxatlarda har bir ishtirokchining ochkolari saqlanadi (bu nuqtadan keyin ikkita belgisi bo‘lgan moddiy sonlar, masalan 4.03). Bitta jamoa ishtirokchisi boshqa jamoaning xuddi shunday raqam ostidagi ishtirokchisi bilan bellashmoqda. Ya’ni birinchi birinchi bilan ikkinchi – ikkinchi bilan v.h.k. bellashmoqda.

Tasodifiy moddiy sonlardan (5 dan 10 gacha) ishtirokchilarning ikkita ro‘yxatini (20 tadan element) yaratadigan dasturni yozing. Buning uchun random modulidan to‘g‘ri keladigan funksiyani toping. Keyin faqat har bir juftlikning go‘liblari kiritiladigan, uchinchi ro‘yxatni yarating.

Misol:

```
Birinchi jamoa: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1, 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
Ikkinchi jamoa: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8, 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]
Davra g‘oliblari: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8, 9.93, 8.25, 7.4, 8.26, 8.91, 7.11, 8.29, 9.52]
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).

## 4-topshiriq. Kesmalar bilan mashq qilamiz
### Nima qilish kerak?
Ingliz alifbosining birinchi yettita harfi saqlanadigan satr berilgan.

`alphabet = 'abcdefg'`

Mana bunday o‘nta natijalarni ekranga chiqaradigan dasturni yozing:

1. Satr nusxasi.
1. Satr elementlari teskari tartibda.
1. Satrning har ikkinchi elementi (shu jumladan eng birinchisi ham).
1. Satrning birinchidan keyingi har ikkinchi elementi.
1. Ikkinchigacha bo‘lgan barcha elementlar.
1. Oxiridan boshlab oxirgidan bitta oldindagigacha barcha elementlar.
1. 3 dan 4 gacha bo‘lgan indekslar ko‘lamidagi barcha elementlar (4 kiritmagan holda).
1. Satrning oxirgi uchta elementlari.
1. 3 dan 4 gacha bo‘lgan indekslar ko‘lamidagi barcha elementlar.
1. Oldingi banddagi shartning o‘zi, faqat teskari tartibda.

Natijalarni olish va chiqarish uchun faqat print buyrug‘i va kesmalardan foydalaning.

Dastur ishlashining natijalari:

```
1: abcdefg
2: gfedcba
3: aceg
4: bdf
5: a
6: g
7: d
8: efg
9: de
10: ed
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- Natijani olish uchun faqat  print va alphabet o‘zgaruvchisining kesmasi ishlatiladi.

## 5-topshiriq. Burilish
### Nima qilish kerak?
Dasturga kirishga h harfi kamida ikki marta uchraydigan satr beriladi. h harfining birinchi va oxirgi paydo bo‘lishi o‘rtasida joylashgan belgilarning ketma-ketligini teskari tartibda buradigan kodni yozing.

1-misol:

```
Satrni kiriting: hqwehrty
Birinchi va oxirgi h o‘rtasidagi ketma-ketlikning burilgani: ewq.
```

2-misol:

```
Satrni kiriting: hh
Birinchi va oxirgi h o‘rtasidagi ketma-ketlikning burilgani: 
```

3-misol:

```
Satrni kiriting: hhqwerh
Birinchi va oxirgi h o‘rtasidagi ketma-ketlikning burilgani: rewqh.
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).

## 6-topshiriq. Ro‘yxatni siqish
### Nima qilish kerak?
N butun tasodifiy sonlar (0 dan 2 gacha) ro‘yxati berilgan. «Ro‘yxatni siqish» ni bajaradigan  — barcha nolli elementlarni massiv oxiriga o‘tkazadigan dasturni yozing. Bunda barcha nol bo‘lmagan elementlar massiv boshida xuddi o‘sha tartibda joylashadi. Keyin ro‘yxatdan barcha nollar o‘chirib tashlanadi.

Misol:

```
Ro‘yxatdagi sonlarning soni: 10
Siqishgacha bo‘lgan ro‘yxat: [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]
Siqishdan keyingi ro‘yxat: [2, 1, 1, 2]
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).

## 7-topshiriq. Ikki o‘lchamli ro‘yxat
### Nima qilish kerak?
Biz avval aytib o‘tgandek, dasturlashda kodni ko‘pincha buyurtmachi talab qilayotgan natijadan kelib chiqqan holda yozish kerak bo‘ladi. Bu safar buyurtmachiga mana bunday ikki o‘lchamli ro‘yxat olish kerak:

`[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]`

Bunday ro‘yxatni yaratadigan va uni ekranga chiqaradigan dasturni yozing. Faqat list comprehensions ishlating.
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Chiqarish formati misolga mos keladi: matnsiz, shunchaki sonlar bilan ikki o‘lchamli ro‘yxat.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).

## 8-topshiriq. O‘yin-kulgi
### Nima qilish kerak?
N cho‘pchalarni chapdan o‘ngga qarab 1 dan N gacha bo‘lgan sonlar bilan raqamlab, bir qatorga joylashtirishdi. Keyin ushbu qator bo‘yicha K toshlarni otishdi. Bunda i-chi tosh L_i dan shu jumladan R_i gacha raqamlar bilan bo‘lgan barcha cho‘plarni urib tushirdi. Qaysi cho‘plar joyida turib qolganini aniqlang.

Kirishga N cho‘plarining soni va K otishlarning  sonini oladigan dasturni yozing. Keyin Left_i, Right_i sonlarining K juftlari keladi, bunda 1 ≤ Left_i ≤ Right_i ≤ N.

Dastur agar  j-chi cho‘p turib qolgan bo‘lsa j-chi belgi “I” bo‘lgan yoki j-chi  cho‘p urib tushurilgan bo‘lsa “.” belgisi bo‘lgan N belgilardan tashkil topgan ketma-ketlikni chiqarishi kerak.

Misol:

```
Cho‘plar soni: 10 
Otishlar soni: 3
1-otish. 8 raqamdan 10 raqamgacha cho‘plar urib tushirildi.
2-otish. 2 raqamdan 5 raqamgacha cho‘plar urib tushirildi.
3-otish. 3 raqamdan 6 raqamgacha cho‘plar urib tushirildi.

Natija: I.....I...
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).

## 9-topshiriq. Ro‘yxatlar ro‘yxati
### Nima qilish kerak?
Mana bunday (ko‘p o‘lchamli bo‘lgan!) ro‘yxat berilgan:

```python
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
```
Barcha ichiga kiritilgan ro‘yxatlarni «ochadigan», ya’ni faqat tashqi ro‘yxatni qoldiradigan kodni yozing. Yechim uchun faqat list comprehensions ishlating. 

`Natija: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]`
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Chiqarish formati javobga mos keladi.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).

## 10-topshiriq. Sezar shifri
### Nima qilish kerak?
Yuliy Sezar o‘zining matnni shifrlash usulidan foydalangan. Har bir harf alifbo bo‘yicha K o‘rindan keyingi keladigan harfga doira bo‘yicha almashtirilgan. Agar rus alifbosi va K = 3 olinsa, biz shifrlashni xohlagan so‘zda  А harfi G harfiga, B harfi esa D harfiga aylanadi.

Foydalanuvchi xabar hamda surilishning qiymatini kiritadi. Ushbu xabarni Sezar shifri yordamida shifrlaydigan dasturni yozing.

Misol:

```
Xabarni kiriting: это питон.
Surilishni kiriting: 3
Shifrlangan xabar: ахс тлхср.
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- Shifrlash algoritmi alohida funksiyaga chiqarilgan.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).
## Uyga vazifada nima baholanadi?
- Uyga vazifa GitLab orqali topshirilgan.
- Jildlar va repozitoriy fayllarining tuzilishi python_basic_uz repozitoriyiga mos keladi.
- Hamma vazifalar main.pyning tegishli jildlari va fayllarida bajarilgan.
- Kommitlarning bayoni anglangan va tushunarli: `111`, `done`, `men qildim` — noto‘g‘ri, `added m15 homework`, `14.3 fix: variables naming` — to‘g‘ri.
- Shunchaki `i` bo‘lmagan, nomlangan indekslar ishlatilgan (batafsil 7.2-videoda).
- Foydalanuvchi tomonidan qo‘shimcha harakatlarsiz, `+1` siz to‘g‘ri sonlar ishlatilgan (bu haqda batafsil 7.4-videoda).
- Kiritish uchun quruq salomlashishsiz, `input` to‘g‘ri rasmiylashtirilgan (bu haqda batafsil 2.3-videoda).
- O‘zgaruvchilar faqat `a`, `b`, `c`, `d` bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 2.3-videoda).
- Vergullardan so‘ng va binar operatsiyalarda bo‘shliqlar (probellar) mavjud.
- Funksiyalarning nomlari va qavslardan keyin bo‘shliqlar yo‘q: `print ()`, `input ()` — noto‘g‘ri, `print()` — to‘g‘ri.
- `if-elif-else` bloklari, sikllar va funksiyalar to‘g‘ri rasmiylashtirilgan, bir darajadagi barcha bloklarda xatboshi bir xil.
- Barcha masalalarda ro‘yxatlarni yaratish uchun `list comprehensions` ishlatilgan.
## Maslahatlar va tavsiyalar
- [PEP8](https://docs.python.org/3.7/reference/expressions.html#operator-precedence) arifmetik amallari ustuvor bo‘lib qoladi. and, or kiritish zarur.
- Python [PEP8](https://www.python.org/dev/peps/pep-0008/) uslubi bo‘yicha ingliz tilidagi qo‘llanma.
- Python [PEP8](https://pep8.ru/doc/pep8/) uslubi bo‘yicha uz tilidagi qo‘llanma.
- [Ichiga kiritilgan funksiyalar ro‘yxati](https://docs.python.org/3.7/library/functions.html).
## Topshiriqlarni qanday qilib tekshirishga jo‘natish lozim?
Uyga vazifani bajarish uchun IDE PyCharm yordamida kompyuteringizdagi python_basic_uz repozitoriysini yangilang. Masalalar Module17 papkasida joylashgan.

Modul uyga vazifalarini Skillbox GitLab servisining Git versiyalarni nazorat qilish tizimi orqali topshiring. Uyga vazifali darsda «Bajarildi» deb yozing va repozitoriyga havolani biriktiring. Repl.it ga havolalarni qoldirish kerak emas.
