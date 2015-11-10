from math import floor
from hashlib import sha1
def arb_hash(n, s):
    i = floor(n/40.0)
    h = sha1(str(n) + s).hexdigest()
    for x in range(int(i)):
        h_prime = sha1(str(n) + h).hexdigest()
        h = h + h_prime
    return h[:n]
