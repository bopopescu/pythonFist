#!E:\thirdplugin\python2.7\python.exe
# -*- coding: UTF-8 -*-

import sys
# print sys.stdin.readline()
# print sys.modules
# print sys.platform
# print sys.path

# import os
# # print os.environ
# print os.getcwd()
# print os.putenv()
# help(object)
# print callable(object)
# print locals()
# print globals()
# print chr(67)
# print oct(23)
# print hex(23)
# print str(object)


# def chageme(mylist):
#     mylist.append([1, 2, 3, 4]);
#     print mylist
#     return
#
#
# mylist = [10, 20, 30];
# chageme(mylist)
# print mylist

# def printinfo(name, age):
#     print "Name:", name
#     print "Age ", age
#     return
#
#
# printinfo(age=50, name='miki'

# def printinfo(arg1, *vartuple):
#     print "输出"
#     print arg1
#     for var in vartuple:
#         print var
#     return ;
#
#
# printinfo(10)
# printinfo(70, 60, 50)


# sum = lambda arg1, arg2: arg1 + arg2;
# print sum(10, 20)

# globvar = 0
#
#
# def set_globvar_to_one():
#     global globvar
#     globvar = 1
#
#
# def print_globvar():
#     print(globvar)
#
#
# set_globvar_to_one()
# print globvar
# print_globvar()


# def reverse(li):
#     for i in range(0, len(li) /2):
#         temp = li[i]
#         li[i] = li[-i-1]
#         li[-i-1] = temp
#
#
# l = [1, 2, 3, 4, 5]
# reverse(l)
# print l

# def reverse(li):
#     for i in range(0, len(li)/ 2):
#         li[i], li[-1-1] = li[-i-1], li[i]


class Employee:
    '所有的员工的积累'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d " % Employee.empCount

    def displayEmployee(self):
        print "Name: ", self.name, ", Salary:", self.salary


# employee = Employee('aaaa', 'bbb')
# employee.displayCount()
# class Test:
#     def prt(runoob):
#         print(runoob)
#         print(runoob.__class__)
#
#
# t = Test()
# t.prt()
# emp1 = Employee("Zara", 2000)
# emp1.name = "wang.txt"
# emp1.salary = 10000
# emp1.displayEmployee()
# emp2 = Employee("Manni", 5000)
# emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount
# print getattr(emp1, 'name')
# print getattr(emp1, 'salary')







































































