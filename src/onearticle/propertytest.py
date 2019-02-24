
# class Cat:
#     def __init__(self, name):
#         self.name = name
# def walk_func(self):
#     print('%s慢慢地走过一片草地' % self.name)
# d1 = Cat('Garfield')
# d2 = Cat('Kitty')
#
# Cat.walk = walk_func
# d1.walk()


# class Fruit:
#     def info(self):
#         print('我是一个水果！重%g' % self.weight)
# class Food:
#     def taste(self):
#         print('不同食物的口感不同..')
#
# class Apple(Fruit, Food):
#     pass
#
#
# a = Apple()
# a.weight = 5.6
# a.info()
# a.taste()










# class User:
#     def __hide(self):
#         print('示范隐藏的hide方法')
#     def getname(self):
#         return self.__name
#     def setname(self, name):
#         if len(name) < 3 or len(name) > 8:
#             raise ValueError('用户名长度必须在3-8之间')
#         self.__name = name
#     name = property(getname, setname)
#     def setage(self,age):
#         if age < 18 or age > 70:
#             raise ValueError('用户年龄必须在18-70之间')
#         self.__age = age
#     def getage(self):
#         return self.__age
#     age = property(getage, setage)
# u = User()
# u.name = 'fkee'
# u._User__hide()



