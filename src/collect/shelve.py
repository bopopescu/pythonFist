
import shelve

d = shelve.open("wang.txt")
d['xx'] = [0, 1, 2]
d.close()




