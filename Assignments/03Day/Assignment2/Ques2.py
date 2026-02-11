user_list = input("Enter elements separated by space: ").split()

print("Alternate elements are:")
for i in range(0, len(user_list), 2):
    print(user_list[i])