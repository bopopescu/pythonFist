

# while True print('Hello world')
# 10 * (1/0)
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops ! That was no valid number . Try again...")
#

import sys

try:
    f = open('workfile')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error : {0}".format(err))
except ValueError:
    print("Could not covert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


