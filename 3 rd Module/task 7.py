round = int(input("Yo'lning uzunligi: "))
time = int(input("Necha soat harakatlandi: "))
speed = int(input("Tezligi qancha: "))
distance = speed * time 
c = distance // round
d = distance % round
print("Bosib o'tilgan masofa: ", c, 'aylana va ', d, 'kilometr')