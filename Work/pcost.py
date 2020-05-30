# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    cost = 0
    with open(filename, "rt") as f:
        reader = csv.reader(f)
        headers = next(reader) # skip headers
        for ticker, nshares, share_cost in reader:
            try:
                cost += int(nshares) * float(share_cost)
            except ValueError:
                print(f"Invalid entries found nshares: {nshares}, share_cost: {share_cost}")

    return cost

cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost: {cost}")