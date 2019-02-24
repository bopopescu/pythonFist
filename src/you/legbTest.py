#coding:utf-8

# def my_sum(*arg):
#     print ('in my_sum')
#     return sum(arg)

# def my_average(*arg):
#     return sum(arg) / len(arg)
#
#
# def dec(func):
#     def in_dec(*arg):
#         print ('in dec arg=', arg)
#         if len(arg) == 0:
#             return 0
#         for val in arg:
#             if not isinstance(val, int):
#                 return 0
#         return func(*arg)
#     return in_dec
#
# my_sum = dec(my_sum)
#
# print (my_sum(1,2,3,4,5))


def deco(func):
    def in_deco():
        print ('in deco')
        func()
    print ('call deco')
    return in_deco


@deco
def bar():

    print ('in bar')


bar()









