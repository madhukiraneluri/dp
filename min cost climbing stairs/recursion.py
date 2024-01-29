def mincost(cost,n):
    if n<2:
        return cost[n]
    return cost[n]+min(mincost(cost,n-1),mincost(cost,n-2))
cost=[10,15,30]
print(min(mincost(cost,len(cost)-1),mincost(cost,len(cost)-2)))