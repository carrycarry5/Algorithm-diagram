# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:48:25 2019

@author: AlanP
"""


def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

arr = [2,3,4]
print(sum(arr))
