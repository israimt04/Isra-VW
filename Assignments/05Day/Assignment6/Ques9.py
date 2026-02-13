text = input("Enter a string: ")

while True:
    print("\nA. Even position characters")
    print("B. Odd position characters")
    print("C. Length of string")
    print("D. Add 'a' at end length times")
    print("E. Exit")

    choice = input("Enter choice: ").upper()

    if choice == "A":
        print(text[1::2])
    elif choice == "B":
        print(text[0::2])
    elif choice == "C":
        print(len(text))
    elif choice == "D":
        print(text + "a" * len(text))
    elif choice == "E":
        break
    else:
        print("Invalid choice")