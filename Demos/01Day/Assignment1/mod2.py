import mod1

n = int(input("Enter the limit:"))

print("Choose an option:")
print("1. Odd Numbers")
print("2. Even Numbers")
print("3. All Numbers")

choice = int(input("Enter your choice:"))

if choice == 1:
    mod1.print_odd(n)
elif choice == 2:
    mod1.print_even(n)
elif choice == 3:
    mod1.print_all(n)
else:
    print("Invalid choice!")
