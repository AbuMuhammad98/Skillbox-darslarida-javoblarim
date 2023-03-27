a = [1, 4, -3, 0, 10]
b = int(input("Surish soni: "))

def Surish(a, b):
    step = 1
    while step <= b :
       n = a[-step:] + a[:-step]
       step += 1
    print(n)
print(Surish(a, b))
