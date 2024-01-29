# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 02:21:38 2024

@author: 91630
"""

def sos(cost,n):
    dp=[-1]*(n)
    dp[0]=cost[0]
    dp[1]=cost[1]
    for i in range(2,n):
        dp[i]=cost[i]+min(dp[i-1],dp[i-2])
    return dp[n-1]
print(sos([30,10,60,10,60,50],6)