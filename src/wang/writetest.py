
import pathlib

p = pathlib.Path('a_test.txt')
result = p.write_text('''
有一个美丽的新世界
他在远方等我
哪里有天真的孩子
有姑娘的就我''', encoding='utf-8')
print(result)

content = p.read_text(encoding='utf-8')
print(content)
print(p.read_bytes())




