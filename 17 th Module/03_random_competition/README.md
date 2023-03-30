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
