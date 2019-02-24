

import fileinput
for line in fileinput.input(files=('a_test.txt', 'guitest.py')):
    print(fileinput.filename(), fileinput.filelineno(), line, end="")
fileinput.close()




