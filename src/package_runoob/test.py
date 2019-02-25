#!E:\thirdplugin\python2.7\python.exe
# -*- coding: UTF-8 -*-

from package_runoob.runoob1 import runoob1
from package_runoob.runoob2 import runoob2
import systest


# runoob1()
# runoob2()


# print "Employee.__doc__:", systest.Employee.__doc__
# print "Employee.__name__:", systest.Employee.__name__
# print "Employee.__module__:", systest.Employee.__module__
# print "Employee.__bases__:", systest.Employee.__bases__
# print "Employee.__dict__:", systest.Employee.__dict__


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, '销毁'


pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)
del pt3
del pt2
del pt1













