def Yillar(a, b):
    if a > b: a, b = b, a
    years = []
    for year in range(a, b+1):
        a1 = year // 1000
        a2 = year // 100 % 10
        a3 = year // 10 % 10
        a4 = year % 10
        if (a1 == a2 and a1 == a3) or (a1 == a2 and a1 == a4) or (a1 == a3 and a1 == a4) or (a2 == a3 and a2 == a4):
            print(year)
a = int(input("Birinchi yilni kiriting: "))
b = int(input("Ikkinchi yilni kiriting: "))
Yillar(a, b)
