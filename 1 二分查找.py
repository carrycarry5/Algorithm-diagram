# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:02:03 2019

@author: AlanP
"""

def binary_search(arr, key):
    head = 0
    tail = len(arr) - 1
     
    while head <= tail:
        mid = int((head + tail)/2)
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            tail = mid-1
        if arr[mid] < key:
            head = mid+1
    return -1

arr = [1,3,5,7,8,9]
key = 9
print(binary_search(arr, key))

