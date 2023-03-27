a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
for i in b:
    a.append(i)
t = 0
for i in a:
    if i == 5:
        t += 1
print(t)
d = []
for i in a:
    if i != 5:
        d.append(i)
for i in c:
    d.append(i)
t = 0
for i in d:
    if i == 3:
        t += 1
print(t)
print(d)

a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
fives = a.count(5)
print(f"Birinchi birlashishda 5 lar soni: {fives} ta")
for sym in a:
    if sym == 5:
        a.remove(5)
a.extend(c)
trees = a.count(3)
print(f"Ikkinchi birlashishda 3 lar soni: {trees}")
print(a)
