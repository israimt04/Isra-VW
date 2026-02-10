def maximum_of_three(x, y, z):
    if x >= y and x >= z:
        return x
    if y >= x and y >= z:
        return y
    return z

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print("Maximum:", maximum_of_three(num1, num2, num3))
