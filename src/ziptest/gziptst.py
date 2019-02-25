
import gzip
import shutil

with open("./wang.txt", 'rb') as f_in:
    with gzip.open("./you.gz", 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


