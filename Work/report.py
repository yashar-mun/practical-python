# report.py

import csv

def read_portfolio(filename):

    portfolio = []

    with open(filename) as file:
        rows = csv.reader(file)
        next(file, None)

        for row in rows:
            item = {'name':row[0],'shares':int(row[1]),'price':float(row[2])}
            portfolio.append(item)

    return portfolio

def read_prices(filename):

    import csv

    rows = csv.reader(open(filename, 'r'))

    prices = {}
    for row in rows:
        try:
            stock = row[0]
            price = row[1]
            prices[stock] = float(price)
        except IndexError:
            pass

    return prices


portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')

list_of_costs = []
for item in portfolio:
    list_of_costs.append(round(item['shares']*item['price'],2))

total_cost = round(sum(list_of_costs),2)
print('Total coat:', total_cost)

list_of_values = []
for item in portfolio:
    list_of_values.append(item['shares']*prices[item['name']])

total_value = round(sum(list_of_values),2)
print('Total value:', total_value)

print('Gain:', round(total_value - total_cost,2))

