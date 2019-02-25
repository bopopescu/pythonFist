
import sys
# print(dir(sys))

s = 'Hello world.'
print(str(s))
print(repr(s))
print(repr(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

print('12'.zfill(5))
print('-3.14'.zfill(7))
import math
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

table = {'Sjoerd':4127, 'Jack':4098,'Dcab':7678}
for name,phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name,phone))


f = open('workfile', 'r+')
print(f.read())


print(dir(f))
f.seek(0)
print(f.readline())

f.seek(0)
for line in f:
    print(line, end='')






















