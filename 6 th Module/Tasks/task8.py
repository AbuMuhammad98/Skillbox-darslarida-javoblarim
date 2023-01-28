# Bankdagi omonat X dollarni tashkil qiladi. U har yili P foizga oshadi, shundan so'ng sentning kasr qismi tashlanadi. Necha yildan keyin omonat kamida Y dollar bo'lishini aniqlang. X, Y, P sonlarni hisobga olgan holda yig‘indi Y qiymatiga yetguncha necha yil o‘tishini aniqlaydigan dastuni tuzing.
omonat = int(input("Omonat miqdorini kiriting: "))
yil = 0
foiz = int(input("Foiz miqdorini kiriting: "))
maqsad = 100000
while True:
    if omonat < maqsad:
        omonat = ((omonat*foiz)/100 + omonat)//1
        yil += 1
    else:
        print(omonat)
        print(f"{yil} yildan so'ng daromadingiz {maqsad} miqdoridan ortadi")
        break
 