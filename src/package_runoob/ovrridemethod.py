#!E:\thirdplugin\python2.7\python.exe
# -*- coding: UTF-8 -*-

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v = Vector(2, 10)
v2 = Vector(5, -2)
print v + v2


class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount

    def count2(self):
        print self.__secretCount


counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter.__secretCount































