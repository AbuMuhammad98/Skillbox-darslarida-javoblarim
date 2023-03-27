first_class = list(range(160, 177, 2))
second_class = list(range(162, 181, 3))
print(first_class)
print(second_class)
first_class.extend(second_class)
print(first_class)

