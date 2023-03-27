## Amaliy mashg‘ulotning maqsadlari
- Skillbox Gitlab servisi bilan hamkorlik qilishni o‘rganish: ma’qullashdan o‘tishni, repozitoriyni klonlashtirishni, interfeysning turli unsurlaridan foydalanishni o‘zlashtirib olish
- IDE PyCharmni o‘rnatish va sozlash.
- Dasturni sozlash uchun breyk-poyntlar va shartli breyk-poyntlarni qo‘llash.
- PyCharmda Python Console interaktiv rejimini ishlatish. 
- PyCharmda  Push, Add, Commit Git-buyruqlaridan foydalanish, amaliy vazifani va o‘qituvchi uchun qarorni to‘g‘ri rasmiylashtirish.
- O‘rganilgan mavzularni takrorlash va funksiyalar hamda haqiqiy sonlar bilan ishlash ko‘nikmalarini mustahkamlash.

## Topshiriqlarga nimalar kiradi
- 1-topshiriq. Tizim haqida axborot.
- 2-topshiriq. Sessiya.
- 3-topshiriq.Yig‘indi va ayirma.
- 4-topshiriq. Teskari son 3.
- 5-topshiriq. Eng kichik bo‘luvchi.
- 6-topshiriq. Tangacha 2.
- 7-topshiriq. Yillar.
## 1-topshiriq. Tizim haqida axborot
### Nima qilish kerak?
Python operasion tizimi va versiyasi haqida axborot to‘plang. Pastdagi koddan main.pyga nusxa oling va ishga tushiring. Shundy bo‘lganda, agar xatolar yuzaga kelsa, o‘qituvchilar sizga yordam berishi osonroq bo‘ladi.

```python
import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
```
### Nima baholanadi?
- Python operasion tizimi va versiyasi haqida axborotga ega «os_info.txt» fayli yaratildi.

## 2-topshiriq. Sessiya
### Nima qilish kerak?
4-darsdagi topshiriqni yeching.

Sinov  topshirish uchun talaba Pyotr dastur yozdi. Dastur ikkita nuqtaning koordinatalari bo‘yicha ushbu ikki nuqtadan o‘tuvchi to‘g‘ri chiziq tenglamasini aniqlaydi: y = k * x + b, bu yerda k va b — burchak koeffisenti va to‘g‘ri chiziqning vertikal siljishini anglatuvchi sonlardir. Dastur quyidagi ko‘rinishga ega:

```python
print("Birinchi nuqtani kiriting")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nIkkinchi nuqtani kiriting")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2
k = y_diff / x_diff
b = y2 - k * x2

print("Ushbu nuqtalar orqali o‘tuvchi to‘g‘ri chiziq tenglamasi:")
print("y = ", k, " * x + ", b)
```
**Dasturning ishlashiga misol (konsolning ichidagilar):**

```bash
Birinchi nuqtani kiriting
X: 10
Y: 20

Ikkinchi nuqtani kiriting
X: 15
Y: 25
Ushbu nuqtalar orqali o'tuvchi to'g'ri chiziq tenglamasi:
y =  1.0  * x +  10.0
```

Biroq sinov topshirish arafasidagi oqshomda Pyotr dastur har doim ham to‘g‘ri ishlayvermasligini bilib qoldi. Masalan, agar birinchi nuqtaning koordinatalari (10, 20)ga teng bo‘lsa, ikkinchi nuqtaning koordinatalari esa (10, 45)ga teng bo‘lsa, dastur to‘g‘ri tenglama bermasdi. Umidsizlikka tushgan va oldinda uyqusiz tun turganini ko‘rgan Pyotr yordam so‘rab, sizga murojaat qildi. To‘g‘ri chiziq tenglamasi barcha hollarda to‘g‘ri tuzilishi uchun, unga koddagi xatoni breyk-poyntlar yordamida topish va to‘g‘rilashga yordam bering.


**Eslatma:**

Agar y = k * x + b ko‘rinishdagi tenglama tuzishning iloji bo‘lmasa, tegishli xabarni chiqaring.


### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifga ega.
- Chiqarib berish shakli misolga to‘g‘ri keladi.

## 3-topshiriq. Yig‘indi va ayirma
### Nima qilish kerak?
Ikkita funksiya yozing. Birinchisi bitta yaxlit musbat N sonini qabul qiladi va sondagi hamma raqamlarning yig‘indisini topadi. Ikkinchisi N sonini qabul qiladi va sondagi raqamlar miqdorini hisoblaydi. Javobda sonlar yig‘indisi va miqdor ayirmasi chiqarib beriladi.


**Dasturning ishlashiga misol:**

```bash
Sonni kiriting: 500

Sonlar yig'indisi: 5
Sondagi raqamlar miqdori: 3
Yig'indi va raqamlar miqdorining ayirmasi: 2
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri taklifga ega.
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- Dastur vazifaning shartida bayon qilingan ikkita alohida funksiyaga ega.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 3.3-videoda).

## 4-son. Teskari son 3
### Nima qilish kerak?
Foydalanuvchi ikkita haqiqiy son — N va Kni kiritadi. Avval butun qismni sonlarga almashtiradigan dastur yozing. Son raqamlar teskari tartibda yozilganligi bilan dastlabki sondan farq qilishi zarur. Keyin dastur kasr qismi bilan xuddi shunday qiladi. Shundan so‘ng sonlar jamlanadi va yig‘indi ekranga chiqariladi.

**Dasturning ishlashiga misol:**
```bash
Birinchi sonni kiriting: 102.12
Ikkinchi sonni kiriting: 123.34

Birinchi son teskari: 201.21
Ikkinchi son teskari: 321.43

Yig'indi: 522.64
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- Asosiy funksional, haqiqiy sonni ag‘darish alohida fuknsiyada tasvirlangan.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 3.3-videoda).
## 5-topshiriq. Eng kichik bo‘luvchi
### Nima qilish kerak?
n>1 butun soni berilgan. Uning 1 dan farq qiluvchi **eng kichik bo‘luvchisi**ni topadigan funksiya yozing.

**Dasturning ishlashiga misol 1:**
```bash
Sonni kiriting: 6
Birdan farq qiluvchi eng kichik bo'luvchi: 2
```
**Dasturning ishlashiga misol 2:**
```bash
Sonni kiriting: 17
Birdan farq qiluvchi eng kichik bo'luvchi: 17
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- Asosiy funksional alohida funksiya(lar)da tasvirlangan.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 3.3-videoda).
## 6-topshiriq. Tangacha 2
### Nima qilish kerak?
Amaliyotchi-shogird berilgan koordinatalar bo‘yicha yana eski metall tangachani topishi zarur. Lekin endi metall qidiruvchi uskuna foydalanuvchining atrofidagi doira ko‘rinishidagi joyni skaner qilmoqda. Metall borligi yoki yo‘qligini aniqlaganda uskuna ekranda tegishli xabarni aks ettirayapti.

Ikkita x va y haqiqiy sonlari hamda r radius berilgan. (x, y) koordinatali nuqta r radiusli doira ichida, uning chegaralarini ham o‘z ichiga olgan holda yotgan-yotmaganligini tekshiruvchi funksiya yozing. Doira markazining koordinatalari — (0, 0). Agar nuqta doiraga tegishli bo‘lsa, “Tangacha qaerdadir shu atrofda” degan xabarni chiqaring. Boshqacha holat bo‘lsa, “Tangacha bu atrofda yo‘q” xabarini chiqaring.


**Dasturning ishlashiga misol 1:** 

```bash
Tangachaning koordinatalarini kiriting:
X: 0.5
Y: 0.5
Radiusni kiriting: 1

Tangacha qaerdadir shu atrofda
```

**Dasturning ishlashiga 2-misol:**

```bash
Tangachanning koordinatalarini kiriting:
X: 2
Y: 2
Radiusni kiriting: 1

Tangacha bu atrofda yo'q
```

### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- Asosiy funksional alohida funksiya(lar)da tasvirlangan.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 3.3-videoda).
## 7-topshiriq. Yillar
### Nima qilish kerak?
Yaqinda Kostya ilmiy-fantastik kitobni o‘qib chiqdi. Unda eng qo‘rqinchli voqealar yilda uchta bir xil raqamlar bo‘lganda ro‘y beradi. Ma’lum bir vaqt oralig‘ida qaysi yillar “alohida” bo‘lgani va bo‘lishi Kostyaga qiziqarli tuyuldi.

Foydalanuvchidan ikkita A va B to‘rt xonali sonlar so‘raladigan dastur yozing. Keyin A dan Bgacha oraliqdagi, yozuvi uchta aynan bir xil raqamlarga ega hamma to‘rt xonali sonlarni o‘sib borish tartibida chiqarib bering.

**Dasturning ishlashiga misol:**

```bash
Birinchi yilni kiriting: 1900
Ikkinchi yilni kiriting: 2100

Uchta bir xil raqamlarga ega bo'lgan, 1900-dan 2100-gacha bo'lgan yillar:
1911
1999
2000
2022
```
### Nima baholanadi?
- Hisoblab chiqishlar natijasi to‘g‘ri.
- Input kiritish uchun to‘g‘ri takliflarga ega. 
- Chiqarib berish shakli misolga to‘g‘ri keladi.
- Asosiy funksional alohida funksiya(lar)da tasvirlangan.
- O‘zgaruvchilar va funksiyalar faqat a, b, c, d bo‘lib qolmagan, ma’noli nomlarga ega (bu haqda batafsil 3.3-videoda).
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


**Rasmiylashtirishning to‘g‘ri varianti:**

```python
if a > 1:
    b = 3
else:
    b = 5
```

**Rasmiylashtirishning noto‘g‘ri varianti:**

```python
if a > 1:
    b = 3
else:
        b = 5
```

- O‘zgaruvchilar to‘g‘ri nomga ega, nom sifatida kiritilgan funksiyalarning nomlari ishlatilmagan  (bu haqda [batafsil kiritilgan funksiyalar ro‘yxatida](https://docs.python.org/3.7/library/functions.html)).

## Maslahatlar va tavsiyalar

- Python va IDE Pycharm interpretatorini [o‘rnatish bo‘yicha yo‘riqnoma](https://docs.google.com/document/d/1S62xm5oE0A56_XYKjpdCiqw4xMlflPNZ8RsP7MYrsss/edit?usp=sharing).
- [PEP8](https://docs.python.org/3.7/reference/expressions.html#operator-precedence) arifmetik operatsiyalari ustuvorlikda qolmoqda. `and`, `or`ni kiritish zarur.
- Python [PEP8](https://www.python.org/dev/peps/pep-0008/) ingliz tilida.
- Python [PEP8](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html) rus tilida.
- [Kiritilgan funksiyalar ro‘yxati](https://docs.python.org/3.7/library/functions.html).
## Vazifani qanday qilib tekshirishga jo‘natish lozim?
Amaliy mashg‘ulotni bajarish uchun, python_basic_uz repozitoriysini IDE PyCharm yordamida o‘z kompyuteringizga ko‘chiring. Vazifalar Module14 jildida joylashgan.

Bu modulning amaliy ishini Skillbox Gitlab servisidagi Git versiyalarni nazorat qilish tizimi orqali topshiring. Amaliy mashg‘ulotli darsda “Bajarildi” deb yozing va repozitoriyga havolani biriktiring. Replitga havolalar qoldirish shart emas.


