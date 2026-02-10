def print_odd(n):
    print("Odd numbers:")
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i, end=" ")
    print()


def print_even(n):
    print("even numbers:")
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

def print_all(n):
    print("All numbers:")
    for i in range(1, n+1):
        print(i, end=" ")
    print()
    