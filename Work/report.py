# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    
    portfolio = []

    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for ticker, nshares, share_price in reader:
            nshares = int(nshares)
            share_price = float(share_price)
            portfolio.append((ticker, nshares, share_price))
    
    return portfolio