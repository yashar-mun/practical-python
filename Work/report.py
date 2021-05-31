# report.py

import fileparse

def read_portfolio(filename):
    print(fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float]))
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])



def read_prices(filename):
    print(fileparse.parse_csv(filename,types=[str,float], has_headers=False))
    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))



def make_report(portfolio, prices):

    report_rows = []

    for item in portfolio:
        report_rows.append((item['name'],item['shares'],round(prices[item['name']],2),
        round(prices[item['name']]-item['price'],2)))

    return report_rows


def print_report(report):
    report.insert(0, ('Name', 'Shares', 'Price', 'Change'))
    dash = '-' * 40
    for i in range(len(report)):
        if i == 0:
            print('{:>10s}{:>10s}{:>10s}{:>10s}'.format(report[i][0],report[i][1],report[i][2],report[i][3]))
            print(dash)
        else:
            print('{:>10s}{:>10d}{:>10.2f}{:>10.2f}'.format(report[i][0],report[i][1],report[i][2],report[i][3]))


def portfolio_report(portfolio_filename, prices_filename):

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)    
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
