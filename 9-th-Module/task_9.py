print('9-topshiriq. Sigirlar')

# Nima qilish kerak

# Sigirlar uchun 10 ta molxona mavjud. Har bir molxonada hayvonlar uchun har xil sharoitlar mavjud, shuning uchun ham ularning  sut berishi farq qiladi. Birinchi molxonada kuniga 2 litr, ikkinchisida 4, uchinchisida - 6, keyin 8, 10, 12, 14, 16, 18, 20 litr.  Ammo hamma xonada ham  sigirlar turmaydi. Bo'sh va band bo'lganlar xonalar  a va b harflari  bilan belgilanadi,
# bu erda a - bo'sh xona, b-band.

# Foydalanuvchining dastur bilan quyidagi o'zaro ta'sirini hisobga olgan holda molxonadan olingan sutni hisoblash uchun dastur yozing: foydalanuvchi 10 ta a va b belgidan iborat qatorni kiritadi . Bir kunda qancha sut ishlab chiqarilishini aniqlash kerak bo'ladi.
milk = 0
for i in range(10):
  string = input('Введите строку из букв a и b, лат. буквами: ')
  if string == 'b':
    milk += 2 * (i + 1)
print('Молока всего: ', milk)
