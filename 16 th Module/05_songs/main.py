violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


muz_num = int(input("Nechta qo'shiqni tanlash lozim: "))
muz_dur_min = 0
muz_dur_sek = 0
for songs in range(muz_num):
    muz_name = input(f"{songs+1}-qo'shiqning nomi: ")
    for song in violator_songs:
        if song[0] == muz_name:
            muz_dur_min += song[1]


print(f"Qo‘shiqlar eshitilib turishining umumiy vaqti: {muz_dur_min} daqiqa")
