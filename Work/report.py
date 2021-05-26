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
        report_rows.append((item['name'],item['shares'],round(prices[item['name']],2),
        round(prices[item['name']]-item['price'],2)))

    return report_rows


portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')    

report = make_report(portfolio, prices)


report.insert(0, ('Name', 'Shares', 'Price', 'Change'))
dash = '-' * 40
for i in range(len(report)):
    if i == 0:
      print('{:>10s}{:>10s}{:>10s}{:>10s}'.format(report[i][0],report[i][1],report[i][2],report[i][3]))
      print(dash)
    else:
      print('{:>10s}{:>10d}{:>10.2f}{:>10.2f}'.format(report[i][0],report[i][1],report[i][2],report[i][3]))
