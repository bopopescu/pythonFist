

from tkinter import *
root = Tk()
root.title('标题')
# w = Label(root, text="Hello Tkinter")
# w.pack()
# root.mainloop()
for i in range(3):
    lab = Label(root, text = '第%d个label' % (i + 1), bg = '#eeeeee')
    lab.pack()
root.mainloop()



# from collections import defaultdict
# s = [('Python', 1), ('swift', 2), ('python', 3), ('swift', 4), ('Python', 9)]
# d = defaultdict(list)
#
# for k, v in s:
#     d[k].append(v)
# print(list(d.items()))

# import itertools as it
#
#
# for e in it.count(10, 3):
#     print(e)
#     if e > 20:
#         break
# print('---------------')
# my_counter = 0
# for e in it.cycle(['Python', 'Kotlin', 'Swift']):
#     print(e)
#     my_counter += 1
#     if my_counter > 7:
#         break
# print('--------')
# for e in it.repeat('Python', 3):
#     print(e)




# from collections import ChainMap
# import builtins
# my_name = '孙悟空'
# def test():
#     my_name = 'yeeku'
#     pylookup = ChainMap(locals(), globals(), vars(builtins))
#     print(pylookup['my_name'])
#     print(pylookup['len'])
#
# test()

# from heapq import *
# my_data = list(range(10))
# my_data.append(0.5)
# print(my_data)
# print(heapify(my_data))
# heappush(my_data, 7.2)
# print(my_data)

import json

# s = json.dumps(['yeeku',{'favorite':('coding', None, 'game',25)}])
# print(s)

# result = json.loads('["yeeku",{"favoriate":["coding", null, "game", 25]}]')
# print(result)

# from collections import deque
# stack = deque(('Kotlin', 'Python'))
# stack.append('Erlang')
# stack.append('Swift')
# print(stack)
# print(stack.pop())
# print(stack.pop())




# import os

# print(os.cpu_count())
# print(os.getpid())
# print(os.sep)
# print(os.getlogin())

# os.system('cmd')
# import time
# print([e for e in dir(time) if not e.startswith('_')])
# print(time.perf_counter())
# print(time.asctime())
# print(time.process_time())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.time())



# import sys
# print([e for e in dir(sys) if not e.startswith('_')])
# print(sys.executable)
# print(sys.getfilesystemencoding())
# print(sys.maxsize)
# print(sys.platform)
# print(sys.version_info)






# import string
#
# print([e for e in dir(string) if not e.startswith('_')])
#
# print(string.__all__)
# print(string.capwords.__doc__)
# print(string.__file__)