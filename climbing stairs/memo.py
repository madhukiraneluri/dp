# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 02:21:38 2024

@author: 91630
"""

def sos(n):
    m={}
    def inner(n):
        if n<=2:
            return n
        if n not in m:
            m[n]=inner(n-1)+inner(n-2)
            return m[n]
        else:
            return m[n]
    return inner(n)
print(sos(5))        