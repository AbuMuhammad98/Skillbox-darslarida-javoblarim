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
