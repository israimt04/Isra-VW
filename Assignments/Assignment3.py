num = input("Enter a 4-digit number: ").strip()
if len(num) != 4 or not num.isdigit():
    print("Please enter a valid 4-digit number")
else:
    digits = [d for d in num]
    print(' '.join(digits))
    place_vals = [str(int(d) * (10 ** (3 - i))) for i, d in enumerate(digits)]
    expanded = ' + '.join(place_vals)
    print(f"{num} = {expanded}")
    reversed_num = ''.join(reversed(digits))
    print(reversed_num)
