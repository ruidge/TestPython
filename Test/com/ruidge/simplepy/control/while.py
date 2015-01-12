#coding=utf-8
'''
Created on 2014-7-14

@author: ruidge
'''

number = 23
running = True

while running:#新语句块总是以冒号作为开始
    #raw_input将输入都看作字符串,input输入有格式,比如整数,浮点,字符串需要用引号包围#
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'Congratulations, you guessed it.' 
#         如果用break则不会走到while语句的else里面,else在判断不成立的条件下执行一次
        break
        running = False # this causes the while loop to stop
    elif (guess < number):
        print 'No, it is a little higher than that' 
    else:
        print 'No, it is a little lower than that' 
else:
    print 'The while loop is over.' 
    # Do anything else you want to do here

print 'Done' , "running is", str(running)
