ish = int(input("Ishlagan soatingiz: "))
kredit_qarz = int(input("Kredit qarzingiz: "))
ovqatlanish = int(input("Ovqatlanish xarajatlari: "))
summ = ish + kredit_qarz + ovqatlanish
if ((200 * ish) / 2 ** 3) + ish >= summ:
    print("Soatlar yetarli, dam olishingiz ,mumkin")
else:
    print("Soatlar yetarli emas, ishlash kerak")