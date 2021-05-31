# pcost.py

import report
import sys


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    total_cost = sum([stock['shares']*stock['price'] for stock in portfolio])
                
    return total_cost

def main(args):
   filename = args[1]
   print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)