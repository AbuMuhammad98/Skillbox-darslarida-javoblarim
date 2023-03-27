size = int(input("Matritsa o'lchamini kiriting: "))
for row in range(size):
  for col in range(size):
    if row < col:
      print(2, ' ', end = "")
    elif row > col:
      print(0, ' ', end = "")
    else:
      print(1, ' ', end = "")
  print()    
# Matritsa o'lchamini kiriting: 5
# 1  2  2  2  2  
# 0  1  2  2  2  
# 0  0  1  2  2  
# 0  0  0  1  2  
# 0  0  0  0  1 