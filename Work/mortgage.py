# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    if month < 12:
        month_payment = payment + 1000
    else:
        month_payment = payment
    month = month + 1
    principal = principal * (1+rate/12) - month_payment
    total_paid = total_paid + payment

print('Total paid', total_paid, 'Months required', month)