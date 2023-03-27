print('5-topshiriq. Ishning chalasi 2')

# Nima qilish kerak?

# Siz hali ham o‘yinlarni ishlab chiquvchi idorada ishlayapsiz va 
# sobiq adabini yegan dasturchining turli dasturlarini tomosha qilayapsiz.
#  Sonli multfilm ishi bilan bog’liq bolalar uchun o‘yinlarning birida siz 
#  quyidagi shartlarga muvofiq kod yozishingiz kerak: kirishda dastur ikkita sonni 
#  qabul qiladi. 

# # Birinchi son kamida uchta raqamdan iborat bo‘lishi kerak, ikkinchi son 
# esa - kamida to‘rtta raqamdan iborat bo‘lishi kerak, aks holda dastur xatolikni 
# chiqaradi. Agar hammasi yaxshi bo‘lsa, unda har bir raqamdagi birinchi va oxirgi 

# raqamlar o‘rin almashadi, keyin ularning yig’indisi chiqariladi.
# # Ana shu yerda siz sobiq dasturchi tomonidan yozilgan va huddi shu masalani hal
#  qiladigan dasturga duch kelasiz! Biroq katta dasturchi sizga bu kodni bir oz 
#  qayta yozishni, shunda u dahshatli ko‘rinmasligini aytadi. Ha yumshoq qilib 
#  aytganda, u sizni ham dahshatga solayapti.
# # Quyidagi dasturni funktsiyalarga ajrating. Takroriy kodlar iloji boricha kam 
# bo‘lishi kerak. Shuningdek, dasturning asosiy qismida faqat sonlarni kiritish, 
# keyin o‘zgartirilgan sonlar va ularning yig’indisini chiqarish mavjudligiga ishonch
 # hosil qiling.

def n_count(num):
    n_count = 0
    while num > 0:
        num //= 10
        n_count += 1
    return n_count

def first_n(num):
    last_d = num % 10
    first_d = num // 10 ** (n_count(num) - 1)
    between_d = num % 10 ** (n_count(num) - 1) // 10
    return last_d * 10 ** (n_count(num) - 1) + between_d * 10 + first_d
     
num = int(input("Birinchi sonni kiriting: "))        
num1 = int(input("Ikkinchi sonni kiriting:"))
print()

if n_count(num) >= 3 and n_count(num1) >= 4: 
        print(f"O'zgartirilgan birinchi son: {first_n(num)}")
        print(f"O'zgartirilgan ikkinchi son: {first_n(num1)}")
        print()
        print(f"Sonlar yig'indisi: {first_n(num) + first_n(num1)}")
elif n_count(num) < 3:
        print("Birinchi sondagi raqamlar 3 tadan kam")
elif n_count(num1) < 4:
        print("Ikkinchi sondagi raqamlar 4 tadan kam")
    



