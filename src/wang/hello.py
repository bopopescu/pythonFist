# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# if __name__ == '__main__':
#     app.run()


import re
import string

# print(re.split(r'\W+','Words, words, words.'))
# print(re.split('[a-f]+','0a3B9', flags=re.IGNORECASE))


# print(re.split(r'\b', 'Words, words, words.'))
# print(re.split(r'\W*', '...words...'))

# print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))

# print(re.escape('python.exe'))
# legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|-:"
# print('[%s]+' % re.escape(legal_chars))

# digits_re = r'\d+'
# sample = '/usr/sbin/sendmail - 0 errors, 12 warnings'
# print(re.sub(digits_re, digits_re.replace('\\', r'\\'), sample))

# import textwrap;
#
# def test():
#     # end first line \ to avoid the empty line !
#     s = '''\
#     hello
#         world
#     '''
#     print(repr(s))
#     print(repr(textwrap.dedent(s)))
#
#
#
# test()

# from datetime import time
from collections import ChainMap
from datetime import time, tzinfo, timedelta
#
# # print(time(hour=12, minute=34, second=56, microsecond=123456).isoformat(timespec='minutes'))
#
# # dt = time(hour=12, minute=34, second=56, microsecond=0)
# # print(dt.isoformat(timespec='microseconds'))
#
#
# class GMT1(tzinfo):
#
#     def utcoffset(self, dt):
#         return timedelta(hours=1)
#
#     def dst(self, dt):
#         return timedelta(0)
#
#     def tzname(self, dt):
#         return "Europe/Prague"
#
#
# t = time(12, 10, 30, tzinfo=GMT1())
# print(t)
#
# gmt = GMT1()
# print(t.isoformat())
# print(t.dst())
# print(t.tzname())
# print(t.strftime("%H:%M:%S %Z"))
# print("The {} is {:%H:%M}".format("time", t))

# import os, argparse
# from collections import ChainMap
#
#
# default = {'color': 'red', 'user': 'guest'}
#
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = {k: v for k, v in vars(namespace).items() if v}
#
# combined = ChainMap(command_line_args, os.environ, default)
# print(combined['color'])
# print(combined['user'])

# from collections import Counter, ChainMap
#
# cnt = Counter()
# for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#     cnt[word] += 1
#
# print(cnt)

#
# from collections import ChainMap
# c = ChainMap()
# d = c.new_child()
# e = c.new_child()
# print(e.maps[0])
# print(e.parents)


# class DeepChainMap(ChainMap):
#     """Variant of ChainMap that allows direct updates to inner scopes"""
#
#     def __setitem__(self, key, value):
#         for mapping in self.maps:
#             if key in mapping:
#                 mapping[key] = value
#                 return
#         self.maps[0][key] = value
#
#     def __delitem__(self, key):
#         for mapping in self.maps:
#             if key in mapping:
#                 del mapping[key]
#                 return
#         raise KeyError(key)
#
#
# d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
# d['lion'] = 'orange'
# d['snake'] = 'red'
# del d['elephant']























































