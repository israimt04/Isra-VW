def overlapping(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False

list1 = [1, 2, 3]
list2 = [4, 5, 3]

print(overlapping(list1, list2))