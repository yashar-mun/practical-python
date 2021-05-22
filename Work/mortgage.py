# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
overpayment = False

while True:
    principal_temp = principal * (1 + rate / 12) - payment
    if principal_temp < 0:
        break

    principal = principal_temp
    total_paid = total_paid + payment
    months = months + 1

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    print(months, round(total_paid,2), round(principal, 2))

if principal_temp < 0:
    print(months + 1, round(principal,2), 0.00)
    print('Total paid', round(total_paid + principal,2), 'in', months + 1, 'months')

else:
    print('Total paid', round(total_paid,2), 'in', months, 'months')
