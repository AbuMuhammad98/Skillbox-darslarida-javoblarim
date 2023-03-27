print('6-topshiriq. Meteostansiya')

# Nima qilish kerak?

# Xalqaro meteostansiya xodimlariga qulaylik yaratish uchun 
# har kuni Selsiy va Farengeyt shkalasi bo‘yicha darajalarning 
# turli moslik jadvallarini chop etish kerak. Selsiy darajalari bo‘yicha 
# uchta butun sonni kirituvchi dastur yozing: quyi harorat chegarasi, yuqori harorat 
# chegarasi va qadam. Dastur belgilangan qadam bilan quyi chegaradan yuqori chegaragacha 
# Selsiy va Farengeyt darajalarining turli moslik jadvalini ko‘rsatadi. Kirish nazoratini ta’minlang. 
# Oxirgi qadam yuqori chegarani hatto "sakrab o‘tgan bo‘lsa" ham chiqarilishi kerak. 
# Ma’lumki, 0C 32F ga to‘g‘ri keladi va har bir Selsiy darajasi 1.8 daraja Farengeytga 
# teng. 

# Misol:
# Kiritish:
# Quyi chegara: 0
# Yuqori chegara: 50
# Qadam: 20
#
# Chiqarish:
# C        F

# 0        32
# 20       68
# 40       104
# 50       122
print("Kiritish: ")
quyi_chegara = int(input("Quyi chegara: "))
yuqori_chegara = int(input("Yuqori chegara: "))
qadam = int(input("Qadam: "))
farangeyt = 0
print()
print("Chiqarish")
print()
print('C','\t', 'F', '\n')
for selsiy in range(quyi_chegara, yuqori_chegara + qadam, qadam):
  if selsiy > yuqori_chegara:
      selsiy = yuqori_chegara
  farangeyt = (selsiy * 1.8) + 32    
  print(selsiy, '\t', farangeyt)
  
     