# coding=utf-8
'''
Created on 2015年3月11日

@author: ruidge
'''
data = [ 20, 3, 2, 1, 40, 23, 54, 5, 56, 7, 9, 89, 10, 7, 6 ]

def bubbleSort(data):
    if(len(data) == 0 or len(data) == 1):
        return ;
    else:
        i = len(data);
        while(i >0):
            j = 0;
            while(j < i - 1):
                if(data[j] > data[j + 1]):
                    temp = data[j + 1]
                    data[j + 1] = data[j]
                    data[j] = temp
                j += 1
            i -= 1
            
    
    
if __name__ == "__main__":
    print data
    bubbleSort(data)
    print data
