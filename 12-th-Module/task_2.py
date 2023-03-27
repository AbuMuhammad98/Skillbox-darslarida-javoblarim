print('2-topshiriq. Funksiya ichidagi funksiya')

# Nima qilish kerak

# Sardor dasturlash bo’yicha maxsus sinov testidan o‘tyapti. U «Funksiyalar» mavzusiga kelmaguncha hammasi yaxshi edi.
# Vazifa quyidagichadir:
# Funksiya sarlavhalarini hisobga olmagan holda dasturning asosiy tarmog'i bir qator koddan iborat. Bu test() funksiyasini chaqirishdir. Unda kiritish uchun butun son so'raladi. Agar u musbat bo'lsa, u holda positive() funksiyasi chaqiriladi, uning tanasida ekranda «Musbat» so'zini ko'rsatish buyrug'i mavjud. Agar son manfiy bo'lsa, negative() funksiyasi chaqiriladi, uning tanasi «Manfiy» so'zini ko'rsatish uchun ifodani o’z ichiga oladi.

# Sardorga yordam bering va shunday dasturni amalga oshiring.
positive = 'Musbat'
negativ = 'Manfiy'

test = int(input("Raqamni kiriting: ")) 
def msb_mfy(test):
  return positive if test > 0 else negativ
print(msb_mfy(test))
print()