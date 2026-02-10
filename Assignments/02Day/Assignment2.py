temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").strip().upper()
if unit == 'C':
    fahrenheit = (temp * 1.8) + 32
    print(f"{temp} C = {fahrenheit} F")
elif unit == 'F':
    celsius = (temp - 32) / 1.8
    print(f"{temp} F = {celsius} C")
else:
    print("Unknown unit. Use C or F.")
