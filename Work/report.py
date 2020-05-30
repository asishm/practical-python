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
            portfolio.append({"name": ticker, "shares": nshares, "price": share_price})
    
    return portfolio

def read_prices(filename):

    prices = {}
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                ticker, price = row
                price = float(price)
                prices[ticker] = price
            except ValueError as e:
                print(f"Skipping row: {row}, error: {e}")
    return prices

portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

portfolio_cost = 0
portfolio_value = 0
for stock in portfolio:
    portfolio_cost += stock['shares'] * stock['price']
    portfolio_value += stock['shares'] * prices[stock['name']]

print(f"Total cost: {portfolio_cost}")
print(f"Total value: {portfolio_value}")
print(f"Net gain/loss: {portfolio_value - portfolio_cost}")