
import hashlib

m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
print(m.digest())

print(hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest())

