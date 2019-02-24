
from pathlib import *

# pp = PurePath('guitest.py')
# print(type(pp))
# pp = PurePosixPath()
# print(pp)
# pp = PurePosixPath('/Users/wangyouzhan/PycharmProjects/pythonFirst/src/wang/iotest.py')
# print(pp.anchor)
# print(pp.drive)
# print(pp.root)
p = Path('.')
for x in p.iterdir():
    print(x)

p = Path('../')
for x in p.glob('**/*.py'):
    print(x)


