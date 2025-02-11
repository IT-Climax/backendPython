materials={
    "cement":500,
    "sand":1000,
    "bricks":2000,
    "steel rods":150
    }
price_per_unit={
    "cement":10,
    "sand":5,
    "bricks":2,
    "steel rods":15
    }
subtotal=0
for x in materials:
    if x =="cement":
        subtotal+=materials[x] *price_per_unit[x]
    elif x =="sand":
        subtotal+=materials[x] * price_per_unit[x]
    elif x=="bricks":
        subtotal+=materials[x]*price_per_unit[x]
    elif x=="steel rods":
        subtotal+=materials[x]*price_per_unit[x]
    else: print("subtotal is {x}")
print(subtotal)

cgpa={
    "a":3.4,
    "b":4.2,
    "c":3.4
}
sum_cgpa=0
for total in cgpa :

    sum_cgpa+=cgpa[total]

    average_cgpa = sum_cgpa / len(cgpa)if average_cgpa> 0 else 0
print( average_cgpa.__round__(2))





#compound interest
#factorial
#pythagoras throrem
#








