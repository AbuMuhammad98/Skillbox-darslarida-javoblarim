print('2-topshiriq. Qarzlar')

# Nima qilish kerak 

# Mirprogbank nihoyat qonunga bo'ysunuvchi fuqarolar va qarzdorlarni ajratib, ularni turli bazalarga joylashtirdi. Ammo bank to'lovchilarga qattiq bosim o'tkazishga shoshilmayapti. Bank operatorlariga ro'yxatdagi har beshinchi qarzdorga qo'ng'iroq qilish (raqamlash noldan boshlanadi) va ularning har biri bankka qancha qarzdorligini aniqlash vazifasi topshirildi. 
# Qarzdorlar soni to'g'risida ma'lumot oladigan  va keyin har beshinchisidan (0 dan boshlab) uning qarzini so'raydigan dasturni yozing. Oxirida qarzlarning umumiy miqdori ko'rsatiladi.

# 1-misol:
# Qarzdorlar sonini kiriting: 13
# 0-raqamli qarzdor
# Qancha qarz? 1000
# 5-raqamli qarzdor
# Qancha qarz? 5000
# 10-raqamli  qarzdor
# Qancha qarz? 2000
# Qarzning umumiy miqdori: 8000
 
# 2-misol:
# Qarzdorlar sonini kiriting: 10
# 0-raqamli qarzdor
# Qancha qarz? 1000
# 5-raqamli qarzdor
# Qancha qarz? 5000
# Qarzning umumiy miqdori: 6000

qarzdorlar = int(input("Qarzdorlar sonini kiriting: "))
umumiy_qarz = 0
for qarzdor in range(0, qarzdorlar+1, 5):
  print(f"{qarzdor} - raqamli qarzdor")
  undiruv = int(input("Qancha qarz: "))
  umumiy_qarz += undiruv

print(f"Umumiy qarzdorlik miqdori: {umumiy_qarz}")