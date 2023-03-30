from random import randint as r

lenght = int(input("Ro'yxatdagi raqamlar soni: "))
lst = [r(0, 2) for _ in range(lenght)]
comp = [i for i in lst if i!= 0]
print(f"Siqishgacha bo'lgan ro'yxat: {lst}")
print(f"Siqishdan keyingi ro'yxat: {comp}")


