# place = int(input("O‘qishga kirayotganlar ro‘yxatidagi o‘rinni kiriting: "))
# ball = int(input("Imtihonlarda olgan ballar sonini kiriting: "))
# stipendiya_bali = 290
# if (ball >= stipendiya_bali) and (place <= 10):
#   print("Tabriklaymiz, Siz o‘qishga kirdingiz! \nBonus sifatida sizga stipendiya hisoblab beriladi.")
# elif (ball < stipendiya_bali) and (place <= 10):
#     print("Tabriklaymiz, Siz o‘qishga kirdingiz! \nLekin stipendiya olish uchun sizda ballar yetishmadi")
# else:
#   print("Afsus, biz faqat 10 kishini o'qishga qabul qilamiz xolos")

place = int(input("O‘qishga kirayotganlar ro‘yxatidagi o‘rinni kiriting: "))
stipendiya_bali = 290
if place <= 10:
  ball = int(input("Imtihonlarda olgan ballar sonini kiriting: "))
  if ball >= stipendiya_bali:
    print(
      "Tabriklaymiz, Siz o‘qishga kirdingiz! \nBonus sifatida sizga stipendiya hisoblab beriladi."
    )
  elif place <= 10:
    if ball < stipendiya_bali:
      print(
        "Tabriklaymiz, Siz o‘qishga kirdingiz! \nLekin stipendiya olish uchun sizda ballar yetishmadi"
      )
  else:
    print("Afsus, biz faqat 10 kishini o'qishga qabul qilamiz xolos")
