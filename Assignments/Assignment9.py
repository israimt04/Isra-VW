year = int(input("Enter a year: "))
is_leap = False
if year % 4 == 0:
    is_leap = True
    if year % 100 == 0 and year % 400 != 0:
        is_leap = False
print("Leap Year" if is_leap else "Not a Leap Year")
