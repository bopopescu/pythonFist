

# s = input('请输入除数：')
# try:
#     result  = 20 / int(s)
#     print('20除以%s的结果是：%g' % (s, result))
# except ValueError:
#     print('值错误，必须输入数值')
# except ArithmeticError:
#     print('算术错误,您不能输入0')
# else:
#     print('没有出现异常')




# import enum
# class Orientation(enum.Enum):
#     EAST = '东'
#     SOUTH = '南'
#     WEST = '西'
#     NORTH = '北'
#     def info(self):
#         print('这是一个代表方向[%s]的枚举' % self.value)
#
# print(Orientation.SOUTH)
# for name, member in Orientation.__members__.items():
#     print(name, '=>', member, ',', member.value)


# class ItemMetaClass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['cal_price'] = lambda self:self.price * self.discount
#         return type.__new__(cls, name, bases, attrs)
# class CellPhone(metaclass=ItemMetaClass):
#     __slots__ = ('price', '_discount')
#     def __init__(self, price):
#         self.price = price
#     @property
#     def discount(self):
#         return self._discount
#     @discount.setter
#     def discount(self, discount):
#         self._discount = discount
#
# cp = CellPhone(2399)
# cp.discount = 0.85
# print(cp.cal_price())


# class Role:
#     pass
#
# r = Role()
# print(type(r))
# print(type(Role))

# def fn(self):
#     print('fn函数')
#
# Dog = type('Dog', (object,), dict(walk=fn, age = 6))
#
# d = Dog()
# print(type(d))
# d.walk()
# class Dog:
#     __slots__ = ('walk', 'age', 'name')
#     def __init__(self, name):
#         self.name = name
#     def test(self):
#         print('预先定义的test方法')
# d = Dog('Snoopy')
# from types import MethodType
#
# d.walk = MethodType(lambda self:print('%s正在慢慢地走' % self.name),d)
# d.age = 5
# d.walk()
# d.foo = 30

