# coding=utf-8
'''
Created on 2015-1-8

@author: zhangrui6
'''
data = [ 20, 3, 2, 1, 40, 23, 54, 5, 56, 7, 9, 89, 10, 7, 6 ]

def insertSort(data):
    if(len(data) == 0 and len(data) == 1):
        return
    else:
        j = 1
        while(j < len(data)):
            keyV = data[j]
            i = j - 1
            while(i >= 0):
                if(data[i + 1] < data[i]):
                    data[i] = data[i + 1]
                    i = i - 1 
                else:
                    break
            data[i + 1] = keyV  
            j = j + 1

def InsertionSort(A):
    j = 1
    while(j < len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
        j = j + 1

if __name__ == '__main__':
    print data
    clone1 = data[:]
    InsertionSort(clone1);
    print clone1
