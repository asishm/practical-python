# pcost.py
#
# Exercise 1.27

cost = 0
with open("./Data/portfolio.csv", "rt") as f:
    next(f) # skip headers
    for line in f:
        ticker, nshares, share_cost = line.split(",")
        cost += int(nshares) * float(share_cost)

print(f"Total cost: {cost}")