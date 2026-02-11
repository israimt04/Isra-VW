my_tuple = (1, 2, 3, 2, 4, 5, 2, 6)

value = int(input("Enter value to find: "))
count = my_tuple.count(value)

if count > 1:
    print("Item is repeated", count, "times")
elif count == 1:
    print("Item found only once")
else:
    print("Item not found")