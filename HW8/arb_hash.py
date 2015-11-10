from hashlib import sha1
def arb_hash(n, s):
    h = sha1(s).hexdigest()
    if(n > len(s)):
        s = s + '0'*(n - len(s))
    return sha1(h + s).hexdigest()[:n]
