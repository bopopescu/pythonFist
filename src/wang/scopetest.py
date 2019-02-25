

import fibo, sys
print(dir(fibo))



# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
#
#
# print(filtered_data)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}? It is {1}.'.format(q, a))


# a = set('abracadabra')
# print(a)

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print('orange' in basket)

# vec = [-4, -2, 0, 2, 4]
# result = [x*2 for x in vec]
# print(result)
# result2 = [x for x in vec if x >= 0]
# print(result2)
# result3 = [abs(x) for x in vec]
# print(result3)

# result = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!=y]
# print(result)

# combs = []
# for x in [ 1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

# while True:
#     print('Hello world')

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#
#
# x = Complex(3.0, -4.5)
# print(x.r)
# print(x.i)


# class MyClass:
#     """A simpele example class"""
#     i = 2345
#
#     def f(self):
#         return 'hello world'


# x = MyClass()
# x.counter = 1
# while x.counter < 10:
    # x.counter = x.counter * 2
# print(x.counter)
# del x.counter
# xf = x.f
# while True:
#     print(xf())

# class Dog:
#
#     kind = 'canine'
#
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)
#
#
# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('Fido')
# e.add_trick('play dead')
# print(d.kind)
# print(e.kind)
# print(d.name)
# print(e.name)
# print(d.tricks)


# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)
#
#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)
#
#     __update = update
#
#
# class MappingSubclass(Mapping):
#
#     def update(self, keys, values):
#         for item in zip(keys, values):
#             self.items_list.append(item)


# m = MappingSubclass([1,2, 3, 4])
# print(m.__dict__)

# for element in [1, 2, 3]:
#     print(element)
#
#
# for element in (1, 2, 3):
#     print(element)
#
#
# for key in {'one':1, 'two': 2}:
#     print(key)
#
# for char in "1234":
#     print(char)


# class Reverse:
#     """Iterator for looping over a sequence backwards"""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
#
#
# rev = Reverse('spam')
# print(iter(rev))

# for char in rev:
#     print(char)
# def reverse(data):
#     for index in range(len(data) - 1, -1, -1):
#         yield data[index]
# for char in reverse('golf'):
#     print(char)

# par = sum(i*i for i in range(10))
# print(par)
# xvec = [10, 20, 30]
# yvec = [7, 5, 3]
# you = sum(x*y for x,y in zip(xvec, yvec))
# print(you)
#
# from math import pi, sin
# sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
# print(sine_table)
#
# unique_words = set(word for line in page for word in line.split())
# print(unique_words)




# print(MyClass.i)
# print(MyClass.f)
# print(MyClass.__doc__)


# def scope_test():
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:",spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
#
# scope_test()
# print("In global scope: ", spam)



