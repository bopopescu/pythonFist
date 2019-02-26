

li = [1, 4, ['2078',12], 6, 7, 9, 11, 14, 16]

import copy

li_a = li.copy()
li_b = copy.deepcopy(li)

li[2].append('wang')
print(li_a)
print(li_b)




# x = len(li)
# print(li[0:x])
# print(li[0:])
# print(li[:x])
# print(li[:])
# print(li[::])
# print(li[-x:x])
# print(li[-x:])




