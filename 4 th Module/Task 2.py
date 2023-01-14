test = int(input("Matematika bo'yicha yig'ilgan ballar: "))
test1 = int(input("Fizika bo'yicha yig'ilgan ballar: "))
test2 = int(input("Ona tili bo'yicha yig'ilgan ballar: "))
budjet = 270
if budjet <= test + test1 + test2:
    print("Tabriklaymiz, siz budjet asosida talabalikkka tavsiya etildingiz.")
else:
    print("Afsuski, siz budjet asosida talabalikka tavsiya etilmadingiz.") 