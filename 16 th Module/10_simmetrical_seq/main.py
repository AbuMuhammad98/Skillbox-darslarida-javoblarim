number = int(input("Sonlar miqdori: "))
lst = []

for i in range(number):
    lst.append(int(input("Son")))

counter = 0
while lst != lst[::-1]:
    lst.insert(number, lst[counter])
    counter += 1

print(f"Sonlarni qo'shib qoyish kerak: {counter}")
print(f"Sonlarning o'zi: {lst[:counter][::-1]}")
print(lst)