#!E:\thirdplugin\python2.7\python.exe
# -*- coding: UTF-8 -*-

# import pprint
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
# 'yellow'], 'blue']]]
#
# pprint.pprint(t, width=30)

# import textwrap
# doc = """The wrap() method is just like fill() except that it return s a list of strings instead of on ebig string with newlines to separate the wrapped lines."""
# print textwrap.fill(doc, width=40)

from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
































































