
def yigindi(num):
    summ = 0
    while num:
        last_num = num % 10
        summ += last_num
        num //= 10
    return summ

def number_count(num):
    num_count = 0
    while num:
        last_num = num % 10
        num_count += 1
        num //=10
    return num_count

num = int(input("Sonni kiriting: "))
a = yigindi(num)
b = number_count(num)
print(f"Sonning raqamlar yig'indisi: {a}")
print(f"Sonnong raqamlar soni: {b}")
print(f"Yig‘indi va raqamlar miqdorining ayirmasi: {a - b}")
