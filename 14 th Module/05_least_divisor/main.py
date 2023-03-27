def EKB(num):
    for i in range(2, num + 1):
        if num % i == 0:
            return i
num = int(input("Sonni kiriting: "))
the_smallest = EKB(num)
print(f"{num} sonining 1 dan katta eng kichik bo'luvchisi: {the_smallest}")

