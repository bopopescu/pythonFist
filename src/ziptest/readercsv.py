

import csv

with open('names.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)




