# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    cost = 0
    with open(filename, "rt") as f:
        next(f) # skip headers
        for line in f:
            ticker, nshares, share_cost = line.split(",")
            cost += int(nshares) * float(share_cost)

    return cost

cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost: {cost}")