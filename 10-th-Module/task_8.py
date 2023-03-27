print('8-vazifa. Piramida')

# Nima qilish kerak

# heshteg belgilari bilan to'ldirilgan teng yonli uchburchak (piramida)ni ekranda aks ettiruvchi dasturni yozing. Piramidaning balandligi foydalanuvchi tomonidan kiritilsin.

# Maslahatlar va tavsiyalar
# Ko'rinish sarlavhasi qanday chiqarilganligini eslang  -----!!!!!!-----

   #
  ###
 #####
#######

hash  = int(input("Piramidaning balandligi: "))


for i in range(hash):
    print(' ' * (hash-i-1) +  '#' * (i*2+1))
  



    