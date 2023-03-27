# 1. 2! = 2. 3! = 6. 4! = 24. 5! = 120. 6! = 720. 7! = 5040. 8! = 40320.
number = int(input("N raqamini kiriting: "))
summ = 1
for num in range(2, number + 1):
    summ *= num
    print(f"{num} sonining faktoriali {summ}")
