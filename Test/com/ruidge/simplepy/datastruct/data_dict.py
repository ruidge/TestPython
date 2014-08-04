#coding=utf-8
'''
Created on 2014-7-21

@author: zhangrui6
'''
ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
             'Larry'     : 'larry@wall.org',
             'Matsumoto' : 'matz@ruby-lang.org',
             'Spammer'   : 'spammer@hotmail.com'
     }

print "Swaroop's address is %s" % ab['Swaroop']

print ab["Larry"]
# print ab["haha"] #KeyError: 'haha'

# Adding a key/value pair
ab['Guido'] = 'guido@python.org'

# Deleting a key/value pair
del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' % len(ab)
# for name, address in ab.items():
#     print 'Contact %s at %s' % (name, address)
for key, value in ab.items(): #D.items() -> list of D's (key, value) pairs, as 2-tuples
    print 'Contact %s at %s' % (key, value)

if 'Guido' in ab: # OR ab.has_key('Guido')
    print "\nGuido's address is %s" % ab['Guido']
    print "Guido's address is %s" % ab.get('Guido')
    
    