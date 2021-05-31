# fileparse.py

import csv

def parse_csv(filename, select=None, types=None, delimiter=',', has_headers=True, silence_errors=True):

    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    with open(filename) as f:
        
        rows = csv.reader(f, delimiter=delimiter)
        
        headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:    
                continue
            
            if indices:
                row = [ row[index] for index in indices ]

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue

            record = dict(zip(headers, row))
            records.append(record)

    return records
