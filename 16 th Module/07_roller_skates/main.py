count_r = int(input("Roliklar soni: "))
size_r = [int(input(f"{i + 1} - juftning o'lchami: ")) for i in range(count_r)]
count_h = int(input("Odamlar soni: "))
size_h = [int(input(f"{i + 1} - odamning o'lchami: ")) for i in range(count_h)]
humans_size = list(set(size_h))
count = 0
for i in humans_size:
    if i in size_r:
        count += 1
print(f"Roliklarni olishi mumkin bo‘lgan eng ko‘p odamlar: {count} nafar")
