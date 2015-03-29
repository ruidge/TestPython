# coding=utf-8
'''
Created on 2015年3月29日

@author: ruidge
'''
data = [ 20, 3, 2, 1, 40, 23, 54, 5, 56, 7, 9, 89, 10, 7, 6 ]

def fastsort(data, leftindex, rightindex):
    if(len(data) == 0 or len(data) == 1):
        return
    if(leftindex < rightindex):
        i = leftindex;
        j = rightindex;
        key = data[rightindex]
        while(i < j):
            while(i < j and data[i] < key):
                i += 1;
            if(i < j):
                data[j] = data[i];
                j -= 1;
            while(i < j and data[j] > key):
                j -= 1;
            if(i < j):
                data[i] = data[j];
                i += 1;
        data[i] = key;
        fastsort(data, leftindex, i - 1);
        fastsort(data, i + 1, rightindex);
        
def binarySearch(data, key):
    if(len(data) == 0):
        return -1;
    if(len(data) == 1):
        return 0;
    i = 0;
    j = len(data) - 1;
    while(i < j):
        mid = (i + j) / 2;
        if(data[mid] == key):
            return mid;
        elif(data[mid] > key):
            j = mid - 1;
            continue
        else:
            i = mid + 1;
            continue
    if(data[i] == key):
        return i;    
    return -1;

if __name__ == "__main__":
    print data
    fastsort(data, 0, len(data) - 1)
    print data
    print binarySearch(data, 111);
    data = [1, 2, 3];
    print binarySearch(data, 3);
    
    
    
