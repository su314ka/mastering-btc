# package : pybitcointools (https://pypi.python.org/pypi/bitcoin written by vitalik
# private key generation by wkim, 2018. 11. 03

import bitcoin.main as btc

import os
import random
import time
import hashlib

# secp256k1 domain paramter (order of G)

N = 115792089237316195423570985008687907852837564279074904382605163141518161494337

# CSPRNG : os.urandom(), random() 
def random_key():
    r = str(os.urandom(32)) \
            + str(random.randrange(2**256)) \
            + str(int(time.time() * 1000000))
    r = bytes(r, 'utf-8')
    h = hashlib.sha256(r).digest()
    key = ''.join('{:02x}'.format(y) for y in h)
    return key


privkey = random_key()
print("\n === privKey Generation ====\n", privkey) 

input("\n\n\t\t if you wanna stop it, pls enter")
