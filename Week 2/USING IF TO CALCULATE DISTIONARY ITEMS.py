

materials = {
    "cement" : 500,
    "sand" : 1000,
    "bricks": 2000,
    "steel rods": 150
}

price_per_unit = {
    "cement": 10,
    "sand": 5,
    "bricks": 2,
    "steel rods": 15
}

subTotal = 0
for product in materials:
    if product == "cement":
        subTotal += materials[product]*price_per_unit[product]
    elif product == "sand":
        subTotal += materials[product]*price_per_unit[product]
    elif product == "bricks":
        subTotal += materials[product]*price_per_unit[product]
    elif product == "steel rods":
        subTotal += materials[product]*price_per_unit[product]
    else:
        print(f"invalid")
print(f"Total is {subTotal}")



