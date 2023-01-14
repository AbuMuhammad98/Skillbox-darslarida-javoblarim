stul1 = int(input("Birinchi mahsulotning narxi: "))
stul2 = int(input("Ikkinchi mahsulot narxi: "))
stul3 = int(input("Uchinchi mahsulot narxi: "))
jami = stul1 + stul2 + stul3
if stul1 + stul2 + stul3 >= 10000:
    chegirma = jami - ((jami*10)/100)
    print("Siz mahsulotlarni 10% chegirma bilan", chegirma, "so'mga xarid qildingiz")
else:
    chegirmasiz = stul1 + stul2 + stul3
    print("Siz mahsulotlarni chegirmasiz", chegirmasiz, "so'mga xarid qildizngiz")
    