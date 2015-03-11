# coding=utf-8
'''
Created on 2015年3月8日

@author: ruidge
'''
from com.ruidge.algorithm.mergesort import mergelist
data = [ 20, 3, 2, 1, 40, 23, 54, 5, 56, 7, 9, 89, 10, 7, 6 ]

def insertSort(data):
    if(len(data) == 0 or len(data) == 1):
        return
    else:
        i = 1
        while(i < len(data)):
            key = data[i]
            j = i
            while(j > 0):
                if(data[j - 1] > key):
                    data[j] = data[j - 1]
                    j -= 1
                else:
                    break
            data[j] = key
            i += 1
    

def mergeSort(data):
    if(len(data) == 0 or len(data) == 1):
        return data
    else:
        mid = len(data) / 2
        leftdata = data[0:mid]
        rightdata = data[mid:]
        return mergelist(mergeSort(leftdata), mergeSort(rightdata))

def mergelist(left, right):
    i = 0
    j = 0
    result = []
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if(i == len(left)):
        result.extend(right[j:])       
    else:
        result.extend(left[i:])       
    return result

def fastSort(data, left, right):
    if(left < right):
        key = data[right]
        i = left
        j = right
        while(i < j):
            while(i < j and data[i] < key):
                i += 1
            if(i < j):
                data[j] = data[i]
                j -= 1
            while(i < j and data[j] > key):
                j -= 1
            if(i < j):
                data[i] = data[j]
                i += 1
#         print i == j
        data[i] = key
        fastSort(data, left, i - 1)
        fastSort(data, i + 1, right)
if __name__ == "__main__":
    c1 = data[:]
    print c1
    insertSort(c1)
    print c1
    
    print "#####"
    c2 = data[:]
    print c2
    print mergeSort(c2)
    
    print "#####"
    c3 = data[:]
    print c3        
    fastSort(c3, 0, len(data) - 1)
    print c3        
