def NoyobHarflar(word):
    letters_count = 0
    for n in list(word):
        if word.count(n) == 1:
            letters_count += 1
    return letters_count
word = input("So'zni kiriting: ")
noyob_harf = NoyobHarflar(word)
print(f"Noyob harflar soni: {noyob_harf}")

def Letters(word):
    return len([n for n in word if word.count(n) == 1])
word = input("So'zni kiriting: ")
noyob_harf = NoyobHarflar(word)
print(f"Noyob harflar soni: {noyob_harf}")