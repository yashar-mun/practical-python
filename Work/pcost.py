# pcost.py

import sys
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as file: 
        rows = csv.reader(file)  
        next(file, None) 
        for row in rows:
            try:             
                total_cost = total_cost + int(row[1]) * float(row[2])
            except ValueError:
                print('Error in:', row)
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
