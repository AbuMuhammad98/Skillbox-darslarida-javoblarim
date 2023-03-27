print("Birinchi nuqtani kiriting")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("-nIkkinchi nuqtani kiriting")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2
if x_diff == 0:
    print("To'g'ri ciziq gorizantal tekislikda yotadi")
elif y_diff == 0:
    print("To'g'ri chiziq vertikal tekislikda yotadi")
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("Ushbu nuqtalar orqali o‘tuvchi to‘g‘ri chiziq tenglamasi:")
    print("y = ", k, " * x + ", b)

