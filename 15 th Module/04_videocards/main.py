def VideoKartaold(num):
    old = []
    for n in range(num):
        print(n + 1, "-", "VideoKartani kiriting: ", end='')
        num_vk = int(input())
        old.append(num_vk)
    return old

num = int(input("Videkartalar sonini kiriting: "))
old_vk = VideoKartaold(num)
print(f"Videokartalarning eski ro'yxati: {old_vk}")
maximum = max(old_vk)
def VideoKartanew(old_vk):
    new = []
    for n in old_vk:
        if n != maximum:
           new.append(n)
    return new
new_vk = VideoKartanew(old_vk)
print(f"Videokartalarning yangi ro'yxati: {new_vk}")
