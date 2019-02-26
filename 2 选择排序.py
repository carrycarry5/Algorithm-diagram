# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:56:21 2019

@author: AlanP
"""

# 简单
def select_sort(arr):
    for i in range(len(arr)):
        k = i
        for j in range(i+1, len(arr)):
            if arr[k] > arr[j]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]
    return arr

arr = [-1,3,5,7,-10,20,-3]
print(select_sort(arr))


# 直观
def find_min(arr):
    min = arr[0]
    j = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            j = i
    return j


def xzpx(arr):
    for i in range(len(arr) - 1):
        min = find_min(arr[i:]) + i
        arr[i], arr[min] = arr[min],arr[i]     
    return arr



arr = [5,8,10,4,-3,100,-5,-100]
print(xzpx(arr))


