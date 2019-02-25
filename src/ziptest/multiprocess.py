

# from multiprocessing import Pool
#
#
# def f(x):
#     return x * x
#
#
# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))

# from multiprocessing import Process
#
#
# def f(name):
#     print('hello', name)
#
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()

#
# from multiprocessing import Process
# import os
#
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process: ', os.getppid())
#     print('process id: ', os.getpid())
#
#
# def f(name):
#     info('function f ')
#     print('hello', name)
#
#
# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()







# import multiprocessing as mp
#
#
# def foo(q):
#     q.put('hello')
#
#
# if __name__ == '__main__':
#     mp.set_start_method('spawn')
#     q = mp.Queue()
#     p = mp.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()


# from multiprocessing import Process, Queue
#
#
# def f(q):
#     q.put([42, None, 'hello'])
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()


#
# from multiprocessing import Process, Pipe
#
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())
#     p.join()



#
# from multiprocessing import Process,Lock
#
#
# def f(l, i):
#     l.acquire()
#     try:
#         print('hello world', i)
#     finally:
#         l.release()
#
#
# if __name__ == '__main__':
#     lock = Lock()
#
#     for num in range(10):
#         Process(target=f, args=(lock, num)).start()



# from multiprocessing import Process, Value, Array
#
#
# def f(n, a):
#     n.value = 3.15927
#     for i in range(len(a)):
#         a[i] = -a[i]
#
#
# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))
#
#     p = Process(target=f, args=(num, arr))
#     p.start()
#     p.join()
#
#     print(num.value)
#     print(arr[:])


#
# from multiprocessing import  Process,Manager
#
#
# def f(d, l):
#     d[1] = '1'
#     d['2'] = 2
#     d[0.25] = None
#     l.reverse()
#
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         d = manager.dict()
#         l = manager.list(range(10))
#
#         p = Process(target=f, args=(d, l))
#         p.start()
#         p.join()
#
#         print(d)
#         print(l)






# from multiprocessing import Pipe
# import array
#
# a, b = Pipe()
# a.send([1, 'hello', None])
# print(b.recv())
# b.send_bytes(b'thank you')
# print(a.recv_bytes())
#
# arr1 = array.array('i', range(5))
# arr2 = array.array('i', [0] * 10)
# a.send_bytes(arr1)
# count = b.recv_bytes_into(arr2)
# print(len(arr1))

# import multiprocessing
#
#
# if __name__ == '__main__':
#         manager = multiprocessing.Manager()
#         Global = manager.Namespace()
#         Global.x = 10
#         Global.y = 'hello'
#         Global._z = 12.3
#         print(Global)


# from multiprocessing.managers import BaseManager
#
#
# class MathsClass:
#     def add(self, x, y):
#         return x + y
#
#     def mul(self, x, y):
#         return  x * y
#
#
# class MyManager(BaseManager):
#     pass
#
#
# MyManager.register('Maths', MathsClass)
#
# if __name__ == '__main__':
#     with MyManager() as manager:
#         maths = manager.Maths()
#         print(maths.add(4, 3))
#         print(maths.mul(7, 8))


# from multiprocessing.managers import BaseManager
# from queue import Queue
# queue = Queue()
#
#
# class QueueManger(BaseManager): pass
#
#
# QueueManger.register('get_queue', callable=lambda:queue)
# m = QueueManger(address=('', 50000), authkey=b'abraceadabra')
# m.connect()
# queue = m.get_queue()
# queue.put('hello')


# from multiprocessing import Pool
# import time
#
#
# def f(x):
#     return x * x
#
#
# if __name__ == '__main__':
#     with Pool(processes=4) as pool:
#         result = pool.apply_async(f, (10,))
#         print(result.get(timeout=1))
#
#         print(pool.map(f, range(10)))
#
#         it = pool.imap(f, range(10))
#         print(next(it))
#         print(next(it))
#         print(it.next(timeout=1))
#
#         result = pool.apply_async(time.sleep, (10,))
#         print(result.get(timeout=1))


# from multiprocessing import Process, Queue
#
#
# def f(q):
#     q.put('X' * 1000000)
#
#
# if __name__ == '__main__':
#     queue = Queue()
#     p = Process(target=f, args=(queue,))
#     p.start()
#     p.join()
#     obj = queue.get()


import multiprocessing
import time
import random
import sys


def calculate(func, args):
    result = func(*args)
    return '%s says that %s%s = %s' % (
        multiprocessing.current_process().name,
        func.__name__, args, result
    )


def calculatestar(args):
    return callable(*args)


def mul(a, b):
    time.sleep(0.5 * random.random())
    return a * b


def plus(a, b):
    time.sleep(0.5 * random.random())
    return a + b


def f(x):
    return 1.0 / (x - 5.0)


def pow3(x):
    return x ** 3


def noop(x):
    pass


def test():
    PROCESSES = 4
    print('Creating pool with %d processes\n' % PROCESSES)

    with multiprocessing.Pool(PROCESSES) as pool:

        TASKS = [(mul, (i, 7)) for i in range(10)] + \
            [(plus, (i, 8)) for i in range(10)]

        results = [pool.apply_async(calculate, t) for t in TASKS]
        imap_it = pool.imap(calculatestar, TASKS)
        imap_unordered_it = pool.imap_unordered(calculatestar, TASKS)

        print('Ordered results using pool.apply_aync():')
        for r in results:
            print('\t', r.get())
        print()

        print('Ordered results using pool.imap():')
        for x in imap_it:
            print('\t', x)
        print()

        print('Unordered results using pool.imap_unordered();')
        for x in imap_unordered_it:
            print('\t', x)
        print()


        # print('Ordered results using pool.map() --')









if __name__ == '__main__':
    multiprocessing.freeze_support()
    test()



















































