# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as file:
        next(file, None) 
        rows = [line.strip().split(',') for line in file]   
        for row in rows:             
            total_cost = total_cost + int(row[1]) * float(row[2])
        return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)

