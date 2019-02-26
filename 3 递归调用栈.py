# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:34:24 2019

@author: AlanP
"""

# 递归调用栈     求阶乘
def func(x):
    if x == 1:
        return 1
    return x * func(x - 1)

print(func(4))


