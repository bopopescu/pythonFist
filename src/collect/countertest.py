

# cnt = Counter()

# for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#     cnt[word] += 1
#
# print(cnt)
# words = re.findall(r'\w+', open('gd_goods.sql', 'r', encoding='utf-8').read().lower())
# print(Counter(words).most_common(10))
# c = Counter()                           # a new, empty counter
# c = Counter('gallahad')                 # a new counter from an iterable
# c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
# c = Counter(cats=4, dogs=8)             # a new counter from keyword args
# print(c)
#
# c = Counter(a=4, b=2, c=0, d=-2)
# d = Counter(a=1, b=2, c=3, d=4)
# print(c.subtract(d))
# print(c)
# from collections import deque
# d = deque('ghi')
# for elem in d:
#     print(elem.upper())
#
# d.append('j')
# d.appendleft('f')
# print(d)
# print(d.pop())
# print(d.popleft())
# print(list(d))
# print(d[0])
# print(d[-1])
# print(list(reversed(d)))
# print('h' in d)
# d.extend('jkl')
# print(d)
#
# deque(['g', 'h', 'i', 'j', 'k'])
# from collections import defaultdict
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)
# for k, v in s:
#     d[k].append(v)
#
# print(sorted(d.items()))
# from collections import defaultdict
#
# s = 'mississippi'
# d = defaultdict(int)
# for k in s:
#     d[k] += 1
#
# print(sorted(d.items()))

# from collections import defaultdict
# def constant_factory(value):
#     return lambda: value
#
#
# d = defaultdict(constant_factory('<missing>'))
# d.update(name='John', action='ran')
# print('%(name)s %(action)s to %(object)s' % d)

# from collections import defaultdict
#
# s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4),('red', 1), ('blue', 4)]
# d = defaultdict(set)
# for k, v in s:
#     d[k].add(v)
#
#
# print(sorted(d.items()))

# from collections import namedtuple
#
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(11, y=22)
# print(p[0] + p[1])
#
# x, y = p
# print(x, y)
# print(p.x + p.y)
# print(p)

# from collections import namedtuple
# import csv
#
# EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
#
# for emp in map(EmployeeRecord._make, csv.reader(open('employees.csv', 'rb', encoding='utf-8'))):
#     print(emp.name, emp.title)
#
#
# import sqlite3
#
# conn = sqlite3.connect('/companydata')
# cursor = conn.cursor()
# cursor.execute('SELECT name, age, title, department, paygrade FROM empoyees')
#
# for emp in map(EmployeeRecord._make, cursor.fetchall()):
#     print(emp.name, emp.title)

# from collections import namedtuple
#
#
# class Point(namedtuple('Point', ['x', 'y'])):
#     __slots__ = ()
#
#     @property
#     def hypot(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#     def __str__(self):
#         return 'Point: x =%6.3f y=%6.3f hypot=%6.3f' % (self.x, self.y, self.hypot)
#
#
# for p in Point(3, 4), Point(14, 5/7):
#     print(p)

# from collections import namedtuple
#
# Book = namedtuple('Book', ['id', 'title', 'authors'])
# Book.__doc__ += ': Hardcover book in active collection'
# Book.id.__doc__ = '13-digit ISBN'
# Book.title.__doc__ = 'Title of first priting'
# Book.authors.__doc__ = 'List of authors sorted by last name'


# from collections import OrderedDict
#
# d = OrderedDict.fromkeys('abcde')
# d.move_to_end('b')
# print(''.join(d.keys()))
# d.move_to_end('b', last=False)
# print(''.join(d.keys()))

# regular unsorted dictionary
# d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
# print(d)
# print(sorted(d.items(), key=lambda t: t[0]))
# print(sorted(d.items(), key=lambda t: t[1]))
# print(sorted(d.items(), key=lambda t: len(t[0])))
# from bisect import bisect
# def grade(score, breakpoints=[60, 70, 80, 90],grades='FDCBA'):
#     i = bisect(breakpoints, score)
#     return grades[i]
#
# # print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
# import weakref
#
#
# class C:
#     def method(self):
#         print("method clled!")
#
#
# c = C()
# r = weakref.ref(c.method)
# r()
# r = weakref.WeakMethod(c.method)
# r()()

# import weakref
#
# class Object:
#     pass
#
#
# o = Object()
# r = weakref.ref(o)
# o2 = r()
# print(o is o2)
# import weakref
#
# _id2obj_dict = weakref.WeakValueDictionary()
#
#
# def remember(obj):
#     oid = id(obj)
#     _id2obj_dict[oid] = obj
#     return oid
#
#
# def id2obj(oid):
#     return _id2obj_dict[oid]


# import pprint
# stuff = ['spam', 'eggs', 'lumberjack', 'knigts', 'ni']
# stuff.insert(0, stuff[:])
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(stuff)
#
# pp = pprint.PrettyPrinter(width=41, compact=True)
# pp.pprint(stuff)

# import pprint

# tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', 'wang.txt')))));
# pp = pprint.PrettyPrinter(depth=6)
# pp.pprint(tup)
# stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
# stuff.insert(0, stuff)
# pprint.pprint(stuff)

# import json
# import pprint
# from urllib.request import urlopen
# with urlopen('http://mobile.weather.com.cn/data/forecast/101010100.html?_=1381891660081') as url:
#     http_info = url.info()
#     raw_data = url.read().decode(http_info.get_content_charset())
# project_info = json.loads(raw_data)
#
# print(project_info)
# pprint.pprint(project_info)
# fom reprlib import recursive_repr
# import reprlib
# import sys
# class MyRepr(reprlib.Repr):
#
#     def repr_TextIOWrapper(self, obj, level):
#         if obj.name in {'<stdin>', '<stdout>', '<stderr>'}:
#             return obj.name
#         return repr(obj)
#
#
# aRepr = MyRepr()
# print(aRepr.repr(sys.stdin))

# from enum import Enum
#
#
# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
#
#
# print(Color.RED)
# print(repr(Color.RED))
#
#
# class Shake(Enum):
#     VANILLA = 7
#     CHOCOLATE = 4
#     COOKIES = 9
#     MINT = 3
#
#
# for shake in Shake:
#     print(shake)
#
#
# print(Shake.VANILLA)
# print(Shake.CHOCOLATE)
# from enum import Enum
#
# Animal = Enum('Animal', 'ANT BEE CAT DOG')
# print(Animal)
# print(Animal.ANT)
# print(Animal.ANT.value)
#
# list(Animal)

# from enum import IntEnum


# class Shape(IntEnum):
#     CIRCLE = 1
#     square = 2
#
#
# class Request(IntEnum):
#     POST = 1
#     GET = 2
#
#
# print(Shape)
# print(Shape.CIRCLE)

# from enum import IntFlag
#
#
# class Perm(IntFlag):
#     R = 4
#     W = 2
#     X = 1
#
#
# print(Perm.R | Perm.W)
#


from enum import Flag, auto





























































































































