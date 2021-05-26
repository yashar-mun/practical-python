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