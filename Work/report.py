# report.py

import csv

def read_portfolio(filename):

    portfolio = []

    with open(filename) as file:
        rows = csv.reader(file)
        next(file, None)

        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)

    return portfolio