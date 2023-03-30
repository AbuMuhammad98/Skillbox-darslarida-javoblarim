sticks = int(input("Choplarning soni: "))
throw = int(input("Otishlarning soni: "))
nishon = ['I'] * sticks

for _ in range(throw):
    print(f"{_ + 1} - otish. ")
    while True:
        left_i = int(input()) - 1
        if (left_i >= 0) and (left_i <= sticks):
            break
    while True:
        right_i = int(input()) - 1
        if (right_i >= left_i) and right_i <= sticks:
            break
    for j in range(left_i, right_i + 1):
        nishon[j] = '.'
print('Natija: ', *nishon, sep='')

