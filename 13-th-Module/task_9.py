# print('9-topshiriq. Annuitet to‘lovi')
#
# # Nima qilish kerak
#
# # i yillik % bilan n yilga berilgan S million rubl miqdoridagi kredit har yilning oxirida foizlar to‘lovlari va asosiy qarz yig’indisini o‘z ichiga olgan teng yillik to‘lovlari to‘lanishi lozim. Foizlar yilda bir marta olinadi. Uchinchi to‘lovni to‘lagandan so‘ng, qarz beruvchi va qarz oluvchi o‘rtasida qarzni to‘lash muddatini n_2 yilga uzaytirish va foiz stavkasini konversiya qilingan paytdan boshlab i_2% ga oshirish to‘g’risidagi kelishuvga erishildi.
#
# # Qarzning qolgan qismini to‘lash rejasini chop etadigan dastur yozing.
# # Quyidagi formulalardan foydalaning (A - annuitet to‘lovining o‘lchami, uning kasr qismini ikkita belgigacha, ya’ni tiyinlargacha yaxlitlang):
#
# # A = KS
#
# # K = i(1 + i) ** n / (1 + i) ** n - 1
#
# # Misol:
#
# # Kredit summasini kiriting: 40e6
# # Necha yilga berilgan? 5    100842
# # Yillik necha foiz? 6
#
# # Davr: 1
# # Davr boshidagi qarz qoldig’i: 40000000.0
# # Foizlar to‘landi: 2400000.0
# # Asosiy kredit to‘landi: 7095856.02
#
# # Davr: 2
# # Davr boshidagi qarz qoldig’i: 32904143.98
# # Foizlar to‘landi: 1974248.6387999998
# # Asosiy kredit to‘landi: 7521607.3812
#
# # Davr: 3
# # Davr boshidagi qarz qoldig’i: 25382536.5988
# # Foizlar to‘landi: 1522952.195928
# # Asosiy kredit to‘landi: 7972903.824072
#
# # Qarz qoldig’i: 17409632.774728
#
# # ======================
#
# # Shartnoma necha yilga uzaytiriladi? 2
# # Stavkani gacha oshirish: 10
#
# # Davr: 1
# # Davr boshidagi qarz qoldig’i: 17409632.774728
# # Foizlar to‘landi: 1740963.2774728
# # Asosiy kredit to‘landi: 3751267.5625271997
#
# # Davr: 2
# # Davr boshidagi qarz qoldig’i: 13658365.2122008
# # Foizlar to‘landi: 1365836.52122008
# # Asosiy kredit to‘landi: 4126394.3187799198
#
# # Davr: 3
# # Davr boshidagi qarz qoldig’i: 9531970.89342088
# # Foizlar to‘landi: 953197.0893420881
# # Asosiy kredit to‘landi: 4539033.750657911
#
# # Davr: 4
# # Davr boshidagi qarz qoldig’i: 4992937.142762969
# # Foizlar to‘landi: 499293.71427629696
# # Asosiy kredit to‘landi: 4992937.125723703
#
# # Qarz qoldig’i: 0.017039266414940357
#
summ = float(input("Kredit summasini kiriting: "))
year = int(input("Necha yilga berilgan?"))
persent = float(input("Yillik necha foiz? "))

def payment(summ, year, percent):
    percent = percent / 100
    k = (percent * (1 + percent) ** year) / ((1 + percent) ** year - 1)
    a_payment = round(k * summ, 2)
    return a_payment

def period_payment(summ, persent, a_payment, period):
    for i in range(1, period + 1):
        paid_persent = summ * persent / 100
        paid_credit = a_payment - paid_persent
        print('\nDavr', i)
        print('\nDavr boshidagi qarz:', summ)
        print("Foizlar to'landi:", paid_persent)
        print("Asosiy kredir to'landi:", paid_credit)
        summ -= paid_credit
    else:
        print("\nAsosiy qarz qoldigi:", summ)

    return summ

a_payment = payment(summ, year, persent)
new_summ = period_payment(summ, persent, a_payment, 3)

new_year = int(input('\nShartnoma necha yilga uzaytirildi? '))
new_percent = float(input('Foizlar qanchaga oshirildi: '))
new_year = new_year + year - 3

a_payment = payment(new_summ, new_year, new_percent)
new_summ = period_payment(new_summ, new_percent, a_payment, new_year)

