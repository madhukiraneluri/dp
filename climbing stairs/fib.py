# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 02:34:45 2024

@author: 91630
"""

def fib(n):
            t1=1
            t2=1
            for i in range(n-1):
                t1,t2=t1+t2,t1
            return t1
print(fib(5))