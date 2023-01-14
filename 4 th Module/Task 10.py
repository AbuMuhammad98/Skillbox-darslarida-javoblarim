number = int(input('Birinchi sonni kirinting: '))
number1 = int(input("Ikkinchi sonni kiriting: "))
number2 = int(input("Uchinchi sonni kiriting: "))

#  Var 1

m = max(number, number1, number2)
print(m)

# Var 2

if number > number1 and number > number2:
    print("'Bular ichida eng yuqorisi': ", number)
else:
    if number1 > number and number1 > number2:
        print("'Bular ichida eng yuqorisi': ", number1)
    else:
        if number2 > number and number2 > number1:
            print("'Bular ichida eng yuqorisi': ", number2)
            
    
            