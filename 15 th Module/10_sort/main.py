def Saralash(lst):
    for min in range(len(lst)):
        for comp in range(min, len(lst)):
            if lst[comp] < lst[min]:
                lst[comp], lst[min] = lst[min], lst[comp]

lst = [1, 4, -3, 0, 10]
Saralash(lst)
print(f"Saralangan ro'yxat: {lst}")