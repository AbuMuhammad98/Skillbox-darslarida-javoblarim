distance = int(input("Bosib o'tilgan masofa: "))
data = int(input("Bugungi sana: "))
summ_distance = (distance // 100) + ((distance // 10) % 10) + (distance % 10)
if summ_distance > data:
    distance -= distance
    print("Sonlarni tashlab yuborish")
    print("Masofa", distance)
else:
    print("Bugun buzilmadi")
    print("Masofa", distance)    