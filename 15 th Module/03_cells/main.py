def Hujayra(num):
    x = []
    for indeks in range(1, num + 1):
        print(indeks, '-', "hujayrani kiriting: ", end=' ')
        element = int(input())
        if element < indeks:
             x.append(element)
    return print("To‘g‘ri kelmaydigan qiymatlar: ", x)
num = int(input("Hujayralar sonini kiriting: "))
Hujayra(num)
