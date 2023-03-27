print('4-vazifa. Krest shakli')

# Nima qilish kerak
  
# "^" belgilari yordamida krest shaklini ekranda namoyish etadigan dasturni yozing
#  (belgilar xayoliy kvadratning diagonallari bo'ylab ko'rsatiladi).

# ^        ^
#  ^      ^ 
#   ^    ^  
#    ^  ^   
#     ^^    
#     ^^    
#    ^  ^   
#   ^    ^  
#  ^      ^ 
# ^        ^
size = int(input("Raqamni kiriting: "))
for row in range(size + 1):
  for col in range(size + 1):
    if col == row: 
      print("^", end = "")
    elif col == -row + size:
      print("^", end = "")
    else:
      print(" ", end = '')
  print()