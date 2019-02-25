import operator
from itertools import accumulate, repeat

# data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
# print(list(accumulate(data, operator.mul)))
# print(list(accumulate(data, max)))

# cashflows = [1000, -90, -90, -90, -90]
# print(list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)))
#
# logistic_map = lambda  x, _: r * x * (1 - x)
# r = 3.8
# x0 = 0.4
# inputs = repeat(x0, 36)
#
# print([format(x, '.2f') for x in accumulate(inputs, logistic_map)])

# from pathlib import Path

# q = Path('.')
# # print([x for x in p.iterdir() if x.is_dir()])
#
# # print(list(p.glob('**/*.py')))
#
# with q.opern() as f:
#     f.readline()

# from pathlib import PureWindowsPath
#
# p = PureWindowsPath('E:/thirdplugin/cocos')
#
# print(p.parts)
# print(p.drive)
# print(p.root)
# print(p.anchor)
# print(p.suffix)
# print(p.stem)

# import os
# from pathlib import Path, PosixPath,PureWindowsPath

# print(os.name)
#
# print(Path('itertools.py'))
# # print(PosixPath('itertools.py'))
# print(PureWindowsPath('itertools.py'))
# print(Path('itertools.py').cwd())
# print(Path('itertools.py').home())


# p = Path('itertools.py')
# p.open('w').write('some text')

# from filecmp import dircmp
#
#
# def print_diff_files(dcmp):
#     for name in dcmp.diff_files:
#         print("diff_file %s found in %s and %s" % (name, dcmp.left, dcmp.right))
#     for sub_dcmp in dcmp.subdirs.values():
#         print_diff_files(sub_dcmp)
#
#
# dcmp = dircmp('F:/zzz')
# print_diff_files(dcmp)















































