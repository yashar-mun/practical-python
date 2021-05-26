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


def make_report(portfolio, prices):

    report_rows = []

    for item in portfolio:
        report_rows.append((item['name'],item['shares'],prices[item['name']],
        prices[item['name']]-item['price']))

    return report_rows


portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')    

report = make_report(portfolio, prices)

for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


