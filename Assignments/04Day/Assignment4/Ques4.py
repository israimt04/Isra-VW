conversions = [
    lambda t: t * 1000,
    lambda kg: kg * 1000,          
    lambda g: g * 1000,            
    lambda mg: mg * 0.00000220462  
]

tonns = float(input("Enter weight in tonns: "))

kg = conversions[0](tonns)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

print(f"{kg} kg")
print(f"{gm} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")