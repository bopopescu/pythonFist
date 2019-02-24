# class Wang(object):
#     hobby = 'Play Computer'
#
#     def __init__(self, name, age, weight):
#         self.name = name
#         self._age = age
#         self.__weight = weight
#
#     @classmethod
#     def get_hobby(cls):
#         return cls.hobby
#
#     @property
#     def get_weight(self):
#         return self.__weight
#
#     def self_introduction(self):
#         print('My Name is %s I am %s years old %s', self.name, self._age)
#
#
# class WangTwo(Wang):
#     def __init__(self, name, age, weight):
#         super(WangTwo, self).__init__(name, age, weight)
#
#     def self_introduction(self):
#         print('child----------')
#
#     def __str__(self):
#         print(self.name)
#
#
# if __name__ == '__main__':
#     wang = WangTwo('Alber', 24, 80)
#     wang.__str__()
#     # print dir(property)
#     # print Wang.get_hobby()
#     # print Wang.get_weight
#     # wang.self_introduction()
