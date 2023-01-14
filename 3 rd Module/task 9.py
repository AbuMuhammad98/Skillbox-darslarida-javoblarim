total = int(input("Tort xonali sonni kiriting: "))
a = total // 1000
b = (total // 100) % 10
c = (total // 10) % 10
d = total % 10
total_1 = d * 1000 + c * 100 + b * 10 + a
print(total_1)