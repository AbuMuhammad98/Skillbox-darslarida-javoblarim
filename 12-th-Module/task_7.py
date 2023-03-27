print('7-topshiriq. Yanami?')

# Nima qilish kerak

# Siz eski do'stingiz bilan yana uchrashdingiz, u vazifani o'sha o'qituvchiga topshirishga yordam berganingiz uchun sizdan juda minnatdor edi. Ammo ushbu do'st hali ham g'amgin ko'rinardi. Siz nima bo'lgani haqida so'raganingizda, do'stingiz hissiyotlar bilan portladi va endi o'qituvchi undan shartli operator va sikllardan foydalanmagan holda minimal sonni topish uchun funksiya yozishni so'raganligini aytdi. 

# Albatta, siz yana bechoraga yordam berishga qaror qildingiz. 
# U uchun shunday dasturni yozing.

def kichik_son(a, b):
  

  return f"Minimal son: {(a // b * b + b // a * b) // (a // b + b // a)}"

print(kichik_son(7, 6))