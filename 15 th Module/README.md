## Amaliy vazifaning maqsadi
- Ma’lumotni Python dasturida ro‘yxat ko‘rinishda taqdim qilishni ishlab chiqish:
  - ro‘yxatga elementlarni qo‘shish;
  - ro‘yxat elementlariga murojaat qilish, ularni o‘zgartirish va ekranga chiqarish.
- Sikl yordamida ro‘yxat bo‘yicha iteratsiyani ishlatishni o‘rganish, ro‘yxat elementlari bilan sikl yordamida ishlash.
- list va len funksiyalarini qanday qo‘llashni tushunib olish.
## Vazifaga nimalar kiradi
- 1-topshiriq. Ro‘yxatni yaratish.
- 2-topshiriq. Musobaqa.
- 3-topshiriq. Hujayralar.
- 4-topshiriq. Videokartalar.
- 5-topshiriq. Kino.
- 6-topshiriq. So‘z tahlili.
- 7-topshiriq. Konteynerlar.
- 8-topshiriq. Yuguruvchi sonlar.
- 9-topshiriq. So‘z tahlili 2.
- 10-topshiriq. Saralash.
## 1-topshiriq. Ro‘yxatni yaratish.
### Nima qilish kerak
N butun soni berilgan. Birdan N gacha bo‘lgan, toq sonlardan tashkil topgan ro‘yxatni shakllantiradigan dasturni yozing.

**1-misol:**

```
Sonni kiriting: 1

Birdan N gacha bo'lgan toq sonlar ro'yxati: [1]
```

**2-misol:**

```
Sonni kiriting: 14

Birdan N gacha bo'lgan toq sonlar ro'yxati: [1, 3, 5, 7, 9, 11, 13]
```

### Nima baholanadi
- Hisoblashlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifnomalarni o‘z ichiga olgan. 
- Chiqarish formati misolga mos keladi.
- O‘zgaruvchilar va funksiyalar faqat `a`, `b`, `c`, `d` emas, balki ma’noli nomlarga ega  (bu haqida 2.3 videosida batafsil).
## 2-topshiriq. Musobaqa 
### Nima qilish kerak
Voleybol bo‘yicha musobaqalar uchun sakkiz kishidan ikki kunga musobaqa jadvalini shakllantirish kerak. Birinchi kunga ishtirokchilar ro‘yxatidan har ikkinchi odamni tanlashga qaror qilishdi.

Sakkizta ismdan iborat ro‘yxat berilgan: Temur, Muhtor, Amir, Siroj, Aziz, Farruh, Kamola, Sitora. Ro‘yxatning faqat juft indeksli elementlarini chiqaradigan dasturni yozing.

**Misol:**

```bash
Birinchi kun: ['Temur', 'Amir', 'Aziz', 'Kamola']
```
### Nima baholanadi
- Hisoblashlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifnomalarni o‘z ichiga olgan. 
- Chiqarish formati misolga mos keladi.
- O‘zgaruvchilar va funksiyalar faqat `a`, `b`, `c`, `d` emas, balki ma’noli nomlarga ega  (bu haqida 2.3 videosida batafsil).

## 3-topshiriq. Hujayralar
### Nima qilish kerak
Ilmiy laboratoriyada yangi turdagi hujayralarni ishlab chiqishmoqda va sinovdan o‘tkazishmoqda. Elementi mahsuldorlik ko‘rsatkichi, indeksi esa – hujayra darajasi bo‘lgan bu N hujayralardan iborat ro‘yxat mavjud. Olimlar hujayralarni quyidagi tamoyil bo‘yicha saralab olishadi: agar hujayraning mahsuldorligi uning darajasidan kam bo‘lsa, u to‘g‘ri kelmaydi.

Ro‘yxat elementlarining qiymati ularning indeksidan kamroq bo‘lgan elementlarini ekranga chiqaradigan dasturni yozing.

**Misol:**

```
Hujayralar soni: 5
1 hujayra mahsuldorligi : 3
2 hujayra mahsuldorligi: 0
3 hujayra mahsuldorligi: 6
4 hujayra mahsuldorligi: 2
5 hujayra mahsuldorligi: 10
 
To'g'ri kelmaydigan qiymatlar: 0 2
```
### Nima baholanadi
- Hisoblashlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifnomalarni o‘z ichiga olgan. 
- Chiqarish formati misolga mos keladi.
- O‘zgaruvchilar va funksiyalar faqat `a`, `b`, `c`, `d` emas, balki ma’noli nomlarga ega  (bu haqida 2.3 videosida batafsil).
## 4-topshiriq. Videokartalar
### Nima qilish kerak
Elektronika do‘konining bazasida NVIDIA kompaniyasining turli avlodlardagi videokartalarining ro‘yxati mavjud. To‘liq nomlar o‘rniga faqat videokarta modeli va avlodini bildiruvchi raqamlar saqlanadi. Kompaniya yaqinda videokartalarning yangi turkumini chiqardi. Eng katta avlodlarni bir necha kunda xarid qilib bo‘lishdi.

Videokartalar ro‘yxatidan eng katta elementlarni o‘chirib tashlaydigan dasturni yozing.

**Misol:**

```
Videokartalar soni: 5
1-videokarta: 3070
2-videokarta: 2060
3- videokarta: 3090
4- videokarta: 3070
5- videokarta: 3090
 
Videokartalarning eski ro'yxati: [ 3070 2060 3090 3070 3090 ]
Videokartalarning yangi ro'yxati: [ 3070 2060 3070 ]
```
### Nima baholanadi
- Hisoblashlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifnomalarni o‘z ichiga olgan. 
- Chiqarish formati misolga mos keladi.
- O'zgaruvchilar va funksiyalar faqat `a`, `b`, `c`, `d` emas, balki ma’noli nomlarga ega  (bu haqida 2.3 videosida batafsil).
## 5-topshiriq. Kino
### Nima qilish kerak
Aziz foydalanuvchilar filmlarga izohlar qoldiradigan, havaskorlar kinosaytiga kirdi. Ularning ro'yxati:

```python
films = ["Qattiq yong'oq", "O'tmishga qaytish", 'Taksichi', 'Leon', 'Bogema rapsodiyasi', 'Gunohlar shahri', 'Memento', 'Otstupnuki', 'Qishloq']
```

Aziz saytga birinchi bor kirishi. U ro‘yxatdan o‘tishni va ularga bo‘lgan izohlarni keyinroq o‘qib chiqish uchun filmlarning bir qismini darhol sevimlilar ro‘yxatiga qo‘shmoqchi.

Foydalanuvchi filmni kiritadigan dasturni yozing. Agar u ro‘yxatda mavjud bo‘lsa, sevimlilar ro‘yxatiga qo‘shiladi. Agar u yo‘q bo‘lsa, xato chiqadi. Oxirida sevimli filmlarning to‘liq ro‘yxatini chiqaring

**Misol:**

```
Nechta fimlarni qo'shishni xohlaysiz? 3
Film nomini kiriting: Leon
Film nomini kiriting: Telba Maks 
Xato: Bizda Telba Maks filmi yo'q :(
Film nomini kiriting: Memento
Sizning sevimli filmlaringiz ro'yxati: Leon, Memento
```

### Nima baholanadi
- Hisoblashlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifnomalarni o‘z ichiga olgan. 
- Chiqarish formati misolga mos keladi.
- O‘zgaruvchilar va funksiyalar faqat `a`, `b`, `c`, `d` emas, balki ma’noli nomlarga ega  (bu haqida 2.3 videosida batafsil).
## 6-topshiriq. So‘z tahlili
### Nima qilish kerak
Neyrotarmoqni mashq qildirish va kerakli matnni yaratish uchun ishlatish maqsadida dastur – so‘zlar tahlilchisini yozing.

Foydalanuvchi so‘zni kiritadi. So‘zdagi noyob harflar sonini hisoblaydigan dasturni yozing. Noyob harflar — bu faqat bir marta uchraydigan harflar.

**1-misol:**

```
So‘zni kiriting: salom

Noyob harflar soni: 5
```

**2-misol:**

```
So‘zni kiriting: lava

Noyob harflar soni: 2
```
### Nima baholanadi
- Hisoblashlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifnomalarni o‘z ichiga olgan. 
- Chiqarish formati misolga mos keladi.
- O‘zgaruvchilar va funksiyalar faqat `a`, `b`, `c`, `d` emas, balki ma’noli nomlarga ega  (bu haqida 2.3 videosida batafsil).
## 7-topshiriq. Konteynerlar 
### Nima qilish kerak
Omborxonada konteynerlar bir qator qilib kilogramdagi vazni o‘smasligi tartibida (kamroq yoki teng) joylashtirilgan. Omborxonaga ma’lum bir joyga qo‘yilishi kerak bo‘lgan, yana bitta konteynerni olib kelishdi.

Kirishga natural sonlarning o‘smaydigan ketma-ketligini qabul qiladigan dasturni yozing. Ular qatordagi har bir konteynerning vaznini bildiradi. Bundan keyin X — yangi konteynerning vazni kirtiladi. Dastur yangi konteyner joylashtiriladigan raqamni chiqaradi. Agar qatorda yangi konteynerning vazni bilan bir xil konteynerlar mavjud bo‘lsa, yangi konteynerni ulardan keyin qo‘yish kerak.

Kiritish nazoratini ta’minlang: barcha sonlar 200 dan oshmaydi.

**Misol:**

```
Konteynerlar soni: 8
Konteyner vaznini kiriting: 165
Konteyner vaznini kiriting: 163
Konteyner vaznini kiriting: 160
Konteyner vaznini kiriting: 160
Konteyner vaznini kiriting: 157
Konteyner vaznini kiriting: 157
Konteyner vaznini kiriting: 155
Konteyner vaznini kiriting: 154
 
Yangi konteynerning vaznini kiriting: 162 
Yangi konteyner oladigan raqam: 3
```
### Nima baholanadi
- Hisoblashlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifnomalarni o‘z ichiga olgan. 
- Chiqarish formati misolga mos keladi.
- O‘zgaruvchilar va funksiyalar faqat `a`, `b`, `c`, `d` emas, balki ma’noli nomlarga ega  (bu haqida 2.3 videosida batafsil).
## 8-topshiriq. Yuguruvchi sonlar
### Nima qilish kerak
Siz bitta matn yoki sonlarning o‘zi siklli ravishda takrorlanadigan kichik tablo uchun dastur yozyapsiz. Masalan, metro, avtobuslar yoki tramvaylardagi kabi.

N elementlardan tashkil topgan ro‘yxat va K butun soni berilgan. Ro‘yxat elementlarini siklli ravishda K pog‘ona o‘ngga suradigan dasturni yozing. O’zlashtirish amallarining iloji boricha kam sonidan foydalaning.

**1-misol:**

```
Surish: 1
Boshlang‘ich ro‘yxat: [1, 2, 3, 4, 5]
Surilgan ro‘yxat: [5, 1, 2, 3, 4]
```

**2-misol:**

```
Surish: 3
Boshlang‘ich ro‘yxat: [1, 4, -3, 0, 10]
Surilgan ro‘yxat: [-3, 0, 10, 1, 4]

```
### Nima baholanadi
- Hisoblashlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifnomalarni o‘z ichiga olgan. 
- Chiqarish formati misolga mos keladi.
- O‘zgaruvchilar va funksiyalar faqat `a`, `b`, `c`, `d` emas, balki ma’noli nomlarga ega  (bu haqida 2.3 videosida batafsil).
## 9-topshiriq. So‘z tahlili 2
### Nima qilish kerak
Matn uchun tahlilchilarni yozishda davom eting. Endi uning yordamida palindromlarni aniqlash mumkin bo‘lgan kodni yozish kerak. Ya’ni chapdan o‘nga ham o‘ngdan chapga ham bir xil o‘qiladigan so‘zlarni topish kerak.

Bunday dasturni yozing.

**1-misol:**

```
So‘zni kiriting: madam

So‘z palindrom 
```

**2-misol:**

```
So‘zni kiriting: abccba

So‘z palindrom 
```

**3-misol:**

```
So‘zni kiriting: abbd

So‘z palindrom emas
```
### Nima baholanadi
- Hisoblashlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifnomalarni o‘z ichiga olgan. 
- Chiqarish formati misolga mos keladi.
- O‘zgaruvchilar va funksiyalar faqat `a`, `b`, `c`, `d` emas, balki ma’noli nomlarga ega  (bu haqida 2.3 videosida batafsil).

## 10-topshiriq. Saralash
### Nima qilish kerak
N sonlardan tashkil topgan ro‘yxat berilgan. Ro‘yxat elementlarini o‘sish bo‘yicha saralab, ularni ekranga chiqaradigan dasturni yozing. Qo‘shimcha ro‘yxatdan foydalanish **mumkin emas**.

Iloji boricha samarali saralash algoritmini o‘ylab topish va yozishga harakat qiling.

**Misol:**

```
Boshlang‘ich ro‘yxat: [1, 4, -3, 0, 10]

Saralangan ro‘yxat: [-3, 0, 1, 4, 10]
```
### Nima baholanadi
- Hisoblashlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifnomalarni o‘z ichiga olgan. 
- Chiqarish formati misolga mos keladi.
- O‘zgaruvchilar va funksiyalar faqat `a`, `b`, `c`, `d` emas, balki ma’noli nomlarga ega  (bu haqida 2.3 videosida batafsil).

## Amaliy mashg‘ulotda nima baholanadi?
- Amaliy vazifa GitLab orqali topshirilgan.
- Jildlar va repozitoriy fayllarining tuzilishi python_basic repozitoriyiga mos keladi.
- Hamma vazifalar `main.py`ning tegishli jildlari va fayllarida bajarilgan.
- Kommitlarning bayoni anglangan va tushunarli: `111`, `done`, `«men qildim»` — noto‘g‘ri, `added m14 homework`, `14.3 fix: variables naming` — to‘g‘ri.
- Shunchaki `i` bo‘lmagan, nomlangan indekslar ishlatilgan (batafsil 8.2-videoda).
- Foydalanuvchi tomonidan qo‘shimcha harakatlarsiz, `+1` siz to‘g‘ri sonlar ishlatilgan (bu haqda batafsil 8.4-videoda).
- Kiritish uchun quruq salomlashishsiz, `input` to‘g‘ri rasmiylashtirilgan (bu haqda batafsil 3.3-videoda).
- O‘zgaruvchilar faqat `a`, `b`, `c`, `d` bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 3.3-videoda).
- Vergullardan so‘ng va binar operatsiyalarda bo‘shliqlar (probellar) mavjud.
- Funksiyalarning nomlari va qavslardan keyin bo‘shliqlar yo‘q: `print ()`, `input ()` — noto‘g‘ri, `print()` — to‘g‘ri.
- `if-elif-else` bloklari, sikllar va funksiyalar to‘g‘ri rasmiylashtirilgan, bir darajadagi barcha bloklarda xatboshi bir xil.

## Maslahatlar va tavsiyalar
- [Rekursiya](https://techrocks.ru/2019/09/15/recursion-demystified/) haqida batafsil
- [PEP8](https://docs.python.org/3.7/reference/expressions.html#operator-precedence) arifmetik amallar ustuvor bo‘lib qoladi. `and`, `or` kiritish zarur.
- Python [PEP8](https://www.python.org/dev/peps/pep-0008/) ingliz tilida.
- Python [PEP8](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html) rus tilida.
- [Kiritilgan funksiyalar ro‘yxati](https://docs.python.org/3.7/library/functions.html).

## Vazifani qanday qilib tekshirishga yuborish mumkin
Uyga vazifani bajarish uchun Basic_collections repozitoriysini IDE PyCharm yordamida o‘z kompyuteringizga ko‘chirib oling. Vazifalar task_ deb nomlangan papkalarda joylashgan.

Modul uyga vazifalarini Skillbox Gitlab servisining Git versiyalarni nazorat qilish tizimi orqali topshiring. Agar barcha testlar muvaffaqiyatli bajarilgan bo‘lsa, bu haqida uyga vazifali darsda yozing va repozitoriyga havolani biriktiring.
