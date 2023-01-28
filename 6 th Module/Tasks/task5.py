# ticket = int(input("Chipta raqamini kiriting: "))
# chipta = ticket
# raqamlar = []
# while ticket != 0:
#   a = ticket % 10
#   raqamlar.append(a)
#   ticket //= 10  
# the_first_three = (raqamlar[0] + raqamlar[1] + raqamlar[2])
# the_last_three = (raqamlar[3] + raqamlar[4] + raqamlar[5])
# if the_first_three == the_last_three:
#     print(f"{chipta} raqamli chipta omadli")
# else:
#     print(f"{chipta} raqamli chipta omadsiz ")


number = int(input("Введите номер билетика: "))
count = 0
sum_left = 0
sum_right = 0

while count != 6:
    slices = number % 10
    if count < 3:
        sum_right += slices
        number //= 10
    else:
        sum_left += slices
        number //= 10
    count += 1
if sum_left == sum_right:
    print('Билет счастливый!')
else:
    print('Не удачный билет!')