print('3-topshiriq. Kalkulyatorni yangilash')

# Nima qilish kerak

# Stepan ham sayyoramiz aholisining aksariyati kabi sonlar yig‘indisi va farqini hisoblash uchun kalkulyatordan foydalanadi. Biroq, u o'z ish jarayonida nafaqat qo'shish va ayirish kabi oddiy harakatlarni bajarishi kerak, balki u allaqachon qo'lda biror narsa qilishdan charchagan. Shu sababli, Stepan o'z kalkulyatori funksiyalarini biroz kengaytirishga qaror qildi. 

# Foydalanuvchiga raqam va u bilan bajarilishi kerak bo'lgan harakatni so'raydigan dasturni yozing: uning raqamlari yig'indisini, maksimal yoki minimal raqamni chiqaring. Har bir harakatni alohida funksiya sifatida yozing, asosiy dasturni esa sikl ko’rinishiga keltiring.

def max_num(number):
    lst = map(int, list(number))
    print( max(lst) )

def min_num(number):
    lst = map(int, list(number))
    print( min(lst) )


def sum_num(number):
    lst = map(int, list(number))
    print ( sum(lst) )
number = input('Raqamni kiriting: ')
while True:
    d = input('Qaysi amalni bajarmnoqchisiz (min, max, sum, stop): ').lower()
    if d == 'min': 
      min_num(number)
    elif d == 'max': 
      max_num(number)
    elif d == 'sum': 
      sum_num(number)
    elif d == 'stop':
      break

    
    
