ob_havo = int(input("Ko'chada havo harorati qanday: "))
meter = 0
while ob_havo > 15:
  meter += 20
  ob_havo -= 2
  if ob_havo <= 15:
     break
  meter += 10
print("Bosib o'tilgan masofa", meter)