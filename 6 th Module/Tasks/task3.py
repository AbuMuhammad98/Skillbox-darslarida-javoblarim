raqam = int(input("Raqamni kiriting: "))
raqamlar_soni = 0
while raqam > 0:
    raqam % 10
    raqamlar_soni +=1
    raqam //=10
print(f"Raqamlar soni: {raqamlar_soni}")
    