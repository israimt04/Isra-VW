list_nums = [1, 2, 3, 4]
tuple_nums = (5, 6, 7, 8)

list_strings = list(map(str, list_nums))
tuple_strings = list(map(str, tuple_nums))

print(list_strings)
print(tuple_strings)