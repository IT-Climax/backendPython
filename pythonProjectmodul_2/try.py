materials = {'cement': 500,
             'sand': 1000,
             'bricks': 2000,
             'steel rod': 150,
             }
price = {'cement': 10,
         'sand': 5,
         'bricks': 2,
         'steel rod': 15,
         }
budget = 0
for X in materials:
    if X == 'sand':
        budget += materials[X] * price[X]
    elif X == 'cement':
        budget += materials[X] * price[X]
    elif X == 'bricks':
        budget += materials[X] * price[X]
    elif X == 'steel rod':
        budget += materials[X] * price[X]
    else:
        print('invalid')
print(budget)
