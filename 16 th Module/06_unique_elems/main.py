first_lang = [int(input("Birinchi ro'yxat uchun son kiriting: ")) for i in range(3)]
second_lang = [int(input("Ikkinchi ro'yxat uchun son kiriting: ")) for i in range(7)]
print(first_lang)
print(second_lang)

first_lang.extend(second_lang)
new_lang = list(set(first_lang))
print(new_lang)

