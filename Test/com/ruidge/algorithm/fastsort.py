# coding=utf-8
'''
Created on 2015年3月8日

@author: ruidge
'''
data = [ 20, 3, 2, 1, 40, 23, 54, 5, 56, 7, 9, 89, 10, 7, 6 ]

def fastsort(data, leftindex, rightindex):
    if(len(data) == 0 or len(data) == 1):
        return data
    if(leftindex < rightindex):
        i = leftindex
        j = rightindex
        key = data[rightindex]
        while (i < j):
            # 小于key的都放到左面,大于key的都放到右面
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
        print i == j
        data[i] = key
        fastsort(data, leftindex, i - 1)
        fastsort(data, i + 1, rightindex)
            

if __name__ == "__main__":
    print data
    fastsort(data, 0, len(data) - 1)
    print data
