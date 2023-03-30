russian_alphabet = ['а', 'б', 'в', 'г',	'д', 'е', 'ё', 'ж',
                    'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
                    'п', 'р', 'с', 'т',	'у', 'ф', 'х', 'ц',
                    'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
                    ]
english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                    ]
message = input("Xabarni kiriting: ").lower()
shift = int(input("Surilishni kiriting: "))
sezar = ''
for i in message:
    if i in russian_alphabet:
        a = russian_alphabet.index(i) + shift
        if russian_alphabet.index(i) + shift >= len(russian_alphabet):
            a = russian_alphabet.index(i) + shift - len(russian_alphabet)

        sezar += (russian_alphabet[a])
    elif i in english_alphabet:
        a = english_alphabet.index(i) + shift
        if english_alphabet.index(i) + shift >= len(english_alphabet):
            a = english_alphabet.index(i) + shift - len(english_alphabet)
        sezar += (english_alphabet[a])
    else:
        sezar += i
print(sezar)