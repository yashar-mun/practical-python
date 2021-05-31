# pcost.py

import report
import sys


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    total_cost = sum([stock['shares']*stock['price'] for stock in portfolio])
                
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename: ')

cost = portfolio_cost(filename)
print('Total cost:', cost)
