# pcost.py

total_cost = 0.0
with open("Data/portfolio.csv") as file:
    next(file, None) 
    rows = [line.strip().split(',') for line in file]   
    for row in rows:             
        total_cost = total_cost + int(row[1]) * float(row[2])
print('Total cost:', total_cost)
