# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
month = 0

while principal > 0:
    month = month + 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        month_payment = payment + extra_payment
    else:
        month_payment = payment
    month_payment = min(month_payment, principal * (1 + rate / 12))
    principal = principal * (1+rate/12) - month_payment
    total_paid = total_paid + month_payment
    print(f"{month:10d} {total_paid:10.2f} {principal:10.2f}")

print(f'Total paid {total_paid:10.2f}\nMonths {month}')