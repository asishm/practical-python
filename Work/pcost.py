# pcost.py
#
# Exercise 1.27
import csv
import sys

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

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")