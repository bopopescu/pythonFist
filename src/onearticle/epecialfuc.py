
# class Fibs:
#     def __init__(self, len):
#         self.first = 0
#         self.sec = 1
#         self.__len = len
#     def __next__(self):
#         if self.__len == 0:
#             raise StopIteration
#         self.first, self.sec = self.sec, self.first + self.sec
#         self.__len -= 1
#         return self.first
#     def __iter__(self):
#         return self
#
# fibs = Fibs(10)
# print(next(fibs))
# for el in fibs:
#     print(el, end=' ')




# def check_key(key):
#     if not isinstance(key, int):raise TypeError('索引值必须是整数')
#     if key < 0: raise IndexError('索引值必须是非负整数')
#     if key >= 26 ** 3: raise IndexError('索引值不能超过%d' % 26 ** 3)
# class StringSeq:
#     def __init__(self):
#         self.__changed = {}
#         self.__deleted = []
#     def __len__(self):
#         return 26 ** 3
#     def __getitem__(self, key):
#         if key in self.__changed:
#             return self.__changed[key]
#         if key in self.__deleted:
#             return  None
#         three = key // (26 * 26)
#         two = (key - three * 26 * 26) // 26
#         one = key % 26
#         return chr(65 + three) + chr(5 + two) + chr(65 + one)
#     def __setitem__(self, key, value):
#         check_key(key)
#         self.__changed[key] = value
#     def __delitem__(self, key):
#         check_key(key)
#         if key not in self.__deleted : self.__deleted.append(key)
#         if key in self.__changed: del  self.__changed[key]
#
# sq = StringSeq()
# print(len(sq))
# print(sq[26 * 26])







# class Role:
#     def __init__(self, name):
#         self.name = name
#     def __call__(self):
#         print('执行Role对象')
# r = Role('管理员')
# r()

# class User:
#     def __init__(self, name, passwd):
#         self.name = name
#         self.passwd = passwd
#     def validLogin(self):
#         print('验证%s的登录' % self.name)
# u = User('crazyit', 'leegang')
# print(hasattr(u.name, '__call__'))
# print(hasattr(u.validLogin, '__call__'))


# class Apple:
#     def __init__(self, color, weight):
#         self.color = color
#         self.weight = weight
#     def __repr__(self):
#         return "App[color=" + self.color + ", weight=" + str(self.weight) + "]"
# a = Apple("红色", 5.68)
# print(a)

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def __del__(self):
#         print('del删除对象')
# im = Item('鼠标', 29.8)
# print(im.__dict__)
# print(dir(im))






