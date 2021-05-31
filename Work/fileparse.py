# fileparse.py

import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        
        headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    
                continue
            
            if indices:
                row = [ row[index] for index in indices ]

            record = dict(zip(headers, row))
            records.append(record)

    return records

portfolio = parse_csv('Data/portfolio.csv', select=['name','shares'])
print(portfolio)