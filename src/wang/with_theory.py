
class FkResource:
    def __init__(self, tag):
        self.tag = tag
        print('构造器，初始化资源： %s' % tag)
    def __enter__(self):
        print('[__enter__] %s' % self.tag)
        return 'fkit'
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('[__exit__ %s] ' % self.tag)
        if exc_tb is None:
            print('没有异常时关闭资源')
        else:
            print('遇到异常时关闭资源')
            return False
with FkResource('孙悟空') as dr:
    print(dr)
    print('1111')
    print('----------------')
with FkResource('白骨精'):
    print('00000')
    raise Exception
    print('---------------')
