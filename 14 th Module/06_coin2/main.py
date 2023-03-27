import math

def Tangacha2(x, y, r):
    if math.sqrt(x**2 + y ** 2) < r:
        return 'Tangacha qayerdadir shu atrofda'
    else:
        return 'Tangcaha bu atrofda yoq'
x = float(input("x kordinatasi: "))
y = float(input("y kordinatasi: "))
r = float(input("r radius: "))
print(Tangacha2(x, y, r))
