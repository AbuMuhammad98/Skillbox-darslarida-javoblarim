people = int(input("Odamlar soni: "))
count = int(input("Sanoqdagi qaysi son? "))
p_lang = list(range(1, people + 1))
out = 0
for i in range(people - 1):
    print(f"Odamlarning joriy doirasi: {p_lang}")
    start_count = out % len(p_lang)
    out = (start_count + count - 1) % len(p_lang)
    print(f"Sanoq {p_lang[start_count]} raqamidan boshlanadi")
    print(f"{p_lang[out]} - raqamli odam chiqib ketadi")
    p_lang.remove(p_lang[out])
    print()

print(f"{p_lang[0]} - raqamli odam qoldi ")
