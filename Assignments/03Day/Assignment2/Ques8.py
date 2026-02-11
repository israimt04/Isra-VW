quantity = int(input("Enter quantity: "))
unit_price = 5

total_price = quantity * unit_price

if quantity > 50:
    total_price = total_price * 0.85   
elif quantity > 30:
    total_price = total_price * 0.90   

print("Total price is: Rs", total_price)