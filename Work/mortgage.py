# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

months = 0

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    months = months + 1

    if months <= 12:
        principal = principal - 1000.0
        total_paid = total_paid + 1000.0

print('Total paid', round(total_paid,2), 'in', months, 'months')
