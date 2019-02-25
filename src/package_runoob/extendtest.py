#!E:\thirdplugin\python2.7\python.exe
# -*- coding: UTF-8 -*-


class Parent:
    parentAttr = 100

    def __init__(self):
        print "call fater constructor"

    def parentMethod(self):
        print "call father method"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "father attr: ", Parent.parentAttr

    def myMethod(self):
        print 'call parent method1'


class Child(Parent):
    def __init__(self):
        print "call child construtor"

    def childMethod(self):
        print "call child method"

    def myMethod(self):
        print 'call child mymethod fuction 1'


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.myMethod()




















