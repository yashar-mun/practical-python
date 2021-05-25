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