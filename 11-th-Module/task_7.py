print("Otning turgan joyini kiriting: ")
x1 = float(input("x: "))
y1 = float(input("y: "))

print("Doskadagi nuqtaning turgan joyini belgilang: ")
x2 = float(input("x: "))
y2 = float(input("y: "))

katak_x1 = int(x1 * 10)
katak_y1 = int(y1 * 10)
print()
katak_x2 = int(x2 * 10)
katak_y2 = int(y2 * 10)
if  (0 < katak_x1 - katak_x2 <= abs(2)) and (0 < katak_y1 - katak_y2 <= abs(2)
    ) or (0 < katak_x2 - katak_x1 <= abs(2)) and (0 < katak_y2 - katak_y1 <= abs(2)):
    print(f"Qafasdagi ot {katak_x1, katak_y1}. Qafasdagi nuqta {katak_x2, katak_y2}")
    print("Ha, ot bu nuqtaga yura oladi")
else:
    print(f"Qafasdagi ot {katak_x1, katak_y1}. Qafasdagi nuqta {katak_x2, katak_y2}")
    print("Yo'q, ot bu nuqtaga yura olmaydi")