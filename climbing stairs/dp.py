# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 02:21:38 2024

@author: 91630
"""

def sos(n):
    dp=[0]*(n+1)
    dp[0]=dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(sos(5))        