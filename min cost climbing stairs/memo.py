def mincost(cost,n,m):
    if n<2:
        return cost[n]
    if n not in m:
        m[n] = cost[n]+min(mincost(cost,n-1,m),mincost(cost,n-2,m))
    return m[n]
cost=[10,15,30]
m={}
print(min(mincost(cost,len(cost)-1,m),mincost(cost,len(cost)-2,m)))