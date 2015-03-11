# coding=utf-8
'''
Created on 2015年1月12日

@author: ruidge
'''
from types import NoneType
data = [ 20, 3, 2, 1, 40, 23, 54, 5, 56, 7, 9, 89, 10, 7, 6 ]

def mergeSort(data):
    if(type(data) is NoneType or len(data) == 0):
        return []
    elif(len(data) == 1):
        return data
    else:
        mid = len(data) / 2
        leftData = data[:mid]
        rightData = data[mid:]
        return mergelist(mergeSort(leftData), mergeSort(rightData))

        
def mergelist(temp1, temp2):
    index1 = 0
    index2 = 0
    result = []
    while(index1 < len(temp1) and index2 < len(temp2)):
        if(temp1[index1] <= temp2[index2]):
            result.append(temp1[index1])
            index1 = index1 + 1
        else:
            result.append(temp2[index2])
            index2 = index2 + 1
    if(index1 == len(temp1)):
        result.extend(temp2[index2:])
    else:
        result.extend(temp1[index1:])
    return result
        
if __name__ == '__main__':
    print data
    cloneData2 = data[:]
    print mergeSort(cloneData2)
