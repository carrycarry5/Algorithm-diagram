# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 15:00:59 2019

@author: AlanP
"""

def quicksort(arr):
    if len(arr) < 2:          # 长度小于2是有序数组
        return arr     
    key = arr[0]
    small = [i for i in arr[1:] if i <= key]
    big = [i for i in arr[1:] if i > key]
    return quicksort(small) + [key] + quicksort(big)

arr = [10,-4,3,6,1,-5]
print(quicksort(arr))




