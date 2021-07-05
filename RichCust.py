def RichestCust(accounts):
    wealth =[]
    for customer in accounts:
        wealth.append(sum(customer))
    return sorted(wealth)[-1]
grid_len = int(input("enter grid length"))
s= [[int(input("Enter number: "))for _ in range(grid_len)] for _ in range(grid_len)]
print(RichestCust(s))
