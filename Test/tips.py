#格式化
print('Age: %s. Gender: %s' % (25, True))

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

#if的判断
x = 0
# x = ""
# x = None
# x = 'None'
# x = -1
if x:
    print('True')
else:
    print('False')

#for的判断
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

if __name__ == '__main__':
    print()