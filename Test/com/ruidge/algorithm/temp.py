# coding=utf-8
'''
Created on 2015年3月8日

@author: ruidge
'''
data = [ 20, 3, 2, 1, 40, 23, 54, 5, 56, 7, 9, 89, 10, 7, 6 ]

def insertSort(data):
    if(len(data) == 0 or len(data) == 1):
        return data
    else:
        j = 1
        while(j<len(data)):
            key = data[j]
            i = j - 1
            #遇到比key大的依次后移
            while(i >= 0):
                if(data[i] > key):
                    data[i+1] = data[i]
                    i -= 1
                else:
                    break
            data[i + 1] = key
            j +=1
    
    
if __name__ == "__main__":
    print data
    insertSort(data)
    print data
