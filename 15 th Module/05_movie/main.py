films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

def Films(films):
    favorite_films = []
    f_movies = int(input("Nechta film kiritmoqchisiz: "))
    for film in range(f_movies):
            print("Film nomini tanlang: ", end='')
            name_film = input().title()
            if name_film in films:
                favorite_films.append(name_film)
            else:
                print(f"Xato: Bizda {name_film} nomli film yo'q")
    return favorite_films
print(Films(films))
