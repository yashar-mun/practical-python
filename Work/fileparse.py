# fileparse.py

import csv

def parse_csv(filename, select=None, types=None, delimiter=','):

    with open(filename) as f:
        
        rows = csv.reader(f, delimiter=delimiter)
        
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

            if types:
                row = [func(val) for func, val in zip(types, row)]

            record = dict(zip(headers, row))
            records.append(record)

    return records
