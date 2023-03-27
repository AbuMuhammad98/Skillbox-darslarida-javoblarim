def Konteyner(numbers):
    konteyner = []
    for number in range(numbers):
        print("Konteyner vaznini kiriting: ", end='')
        weight = int(input())
        konteyner.append(weight)
    return konteyner


numbers = int(input("Konteynerlar soni: "))
konteyner = Konteyner(numbers)
new_konteyner = int(input("Yangi konteyner vaznini kiriting: "))
sort = 0
while sort < len(konteyner) and konteyner[sort] >=new_konteyner:
    sort += 1
print("Yangi konteyner oladigan raqam: ", sort + 1)
