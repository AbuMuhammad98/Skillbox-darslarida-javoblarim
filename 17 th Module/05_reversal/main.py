text = input("Satrni kiriting: ")
index = [position for position, sym in enumerate(text) if sym == 'h']   # https://www.w3schools.com/python/ref_func_enumerate.asp
start = index[0]
end = index[len(index) - 1] - 1
print(f"Birinchi va oxirgi h o‘rtasidagi ketma-ketlikning burilgani: {text[end:start:-1]}")