# coding=utf-8
'''
Created on 2015年3月11日

@author: ruidge
'''
data = [ 20, 3, 2, 1, 40, 23, 54, 5, 56, 7, 9, 89, 10, 7, 6 ]

def selectSort(data):
    if(len(data) == 0 or len(data) == 1):
        return ;
    else:
        i = 0;
        while(i < len(data)):
            j = i + 1;
            while(j < len(data)):
                if(data[j] < data[i]):
                    temp = data[j]
                    data[j ] = data[i]
                    data[i] = temp
                j += 1
            i += 1
            
    
    
if __name__ == "__main__":
    print data
    selectSort(data)
    print data
