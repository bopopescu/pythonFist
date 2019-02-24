

class Cell:
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'

    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'
c = Cell()
c.state = 'Alive'
print(c.state)
print(c.is_dead)



# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def setsize(self, size):
#         self.width, self.height = size
#
#     def getsize(self):
#         return self.width, self.height
#
#     def delsize(self):
#         self.width, self.height = 0,0
#     size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')
#
# print(Rectangle.size.__doc__)
# help(Rectangle.size)
#
# rect = Rectangle(4, 3)
# print(rect.size)
# rect.size = 9,7
# print(rect.width)
# print(rect.height)

# class Inventory:
#     item = '鼠标'
#     quantity = 2000
#     def change(self, item, quantity):
#         self.item = item
#         self.quantity = quantity
# iv = Inventory()
# iv.change('显示器', 500)
# print(iv.item)
# print(iv.quantity)
# print(Inventory.item)
# print(Inventory.quantity)

# global_fn = lambda  p: print('执行lambda表达式，p参数：',p)
# class Category:
#     cate_fn = lambda p: print('执行lambda表达式，p参数', p)
# global_fn('fkit')

# def auth(fn):
#     def auth_fun(*args):
#         print("--------模拟执行权限检查------")
#         fn(*args)
#     return auth_fun
# @auth
# def test(a, b):
#     print("执行test函数...%s---%s" % (a,b))
#
# test(20, 15)



# class Person:
#     hair = 'black'
#
#     def __init__(self, name = 'Charlie', age = 10):
#         self.name = name
#         self.age = age
#
#     def say(self, content):
#         print(content)
#
# p = Person()
# p.skills= ['programming', 'swimming']
# print(p.skills)
# print(p.name)
# def test():
#     age = 20
#     # print(age)
#     print(locals())
#     print(locals()['age'])
#
#
# x = 5
# y = 20
# print(globals())
#
# test()

# def bar(book, price ,desc):
#     print(book, "价格:", price)
#
# my_dict = {"price":89, "book":"疯狂Python讲义","desc":"系统"}
# bar(**my_dict)
# def test(a, *books):
#     print(books)
#     for b in books:
#         print(b)
#     print(a)
#
# test(5, "疯狂ios讲义","疯狂java讲义")

# def my_max(x, y):
#     '''
#     获取两个数值之间的较大数的函数
#     :param x:
#     :param y:
#     :return:
#     '''
#     z = x if x > y else y
#     return z
#
# # print(help(my_max))
# print(my_max.__doc__)


# books = ['疯狂KOtlin讲义','疯狂Swift讲义', '疯狂Python讲义']
# prices = [79, 69, 89]
# for book, price in zip(books, prices):
#     print("%s的价格是：%5.2f" % (book, price))
#
#
# a = range(10)
# print([x for x in reversed(a)])

# import math
#
# print('The value of pi is approximately %5.3f.' % math.pi)
#
# table = {'Sjoerd': 4127, "Jack": 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name:10} ==> {phone: 10d}')
#
#
# print('We are the {} who say "{}!"'.format('knights', 'Ni'))
#
#
# b3 = b'hello'
# b4 = bytes('我们的家乡', encoding='utf-8')
# print(b4)

# a = 2
# print(id(a))

# a_tuple = ('crazyit', 20, 5.6, 'fkit', -7)
# print(a_tuple)
# print(a_tuple[-3: -1])



# a_tuple = ('crazyit', 20, -1.2)
# b_tuple = (127, 'crazyit', 'fkit', 3.33)
# sum_tuple = a_tuple + b_tuple
# print(sum_tuple)
# print(a_tuple + (-20, -30))
# print(1.2 in a_tuple)

# print(dir(list))

# a_list = [2, 30, 'a', [5, 30], 30]
# print(a_list.count(30))


# s_age = input("please input number:")
# age = int(s_age)
# if age > 20:
#     print("the age is bigger than 20.")
#     print("asdfasdfd")


# src_list = {12, 45, 34, 13, 100, 24, 56, 74, 109}
# a_list = []
# b_list = []
# c_list = []
# while len(src_list) > 0:
#     ele = src_list.pop()
#     if ele % 3 == 0:
#         a_list.append(ele)
#     elif ele % 3 == 1:
#         b_list.append(ele)
#     else:
#         c_list.append(ele)
#
#
# print(a_list)
# print(b_list)
# print(c_list)








