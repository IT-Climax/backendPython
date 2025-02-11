materials = {'cement': 500, 'sand': 1000, 'bricks': 2000, 'steel rod': 150, }
price = {'cement': 10, 'sand': 5, 'bricks': 2, 'steel rod': 15, }

budget = 0
for items in materials:
    if items == 'cement':
        budget += materials[items] * price[items]
    else:
        print('invalid')
