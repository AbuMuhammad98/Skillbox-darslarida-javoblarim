print('9-topshiriq. Ifoda')

# Nima qilish kerak

# x soni berilgan. Quyidagi ifodani hisoblash uchun dastur yozing:

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 

# Maslahatlar va tavsiyalar
# surat va maxrajdagi ketma-ketlikka e'tibor bering. Ushbu ketma-ketlik 1, 3, 5, 7 … 63 va 2, 4, 6, 8 … 64 ortib boruvchi arifmetik ketma-ketlik emas.
# Введите икс: 10
# Значение выражения: 1.5370501893939394
surat = 1
maxraj = 1
x = int(input("Raqamni kiriting: "))
for num in range(1, 7):
  surat *= (x-(2 ** num - 1))
  maxraj *= (x-(2 ** num))  
  if surat == 0 or maxraj == 0:
    print(0)
    break

    # print(f"Surat: {surat}")
    # print(f"Maxraj: {maxraj}")

    
print(f"Bo'linma: {surat/maxraj}")
