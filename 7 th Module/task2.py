first = int(input("Boshlang'ich chegarani kiriting: "))
last = int(input("Yakuniy chegarani kiriting: "))
for number in range(first, last + 1):
  if (number % 2 == 0) and (number >= 0):
    print(f"{number} raqami juft va musbat son")
  elif (number % 2 != 0) and (number >= 0):
    print(f"{number} raqami juft emas, lekin musbat son")  
  elif (number % 2 == 0) and (number < 0):
    print(f"{number} raqami juft, ammo musbat emas")
  else:
    print(f"{number} juft ham musbat son ham emas")