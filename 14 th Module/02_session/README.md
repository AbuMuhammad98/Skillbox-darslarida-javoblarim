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