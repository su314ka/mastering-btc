# after generating public key, make compressed or uncompressed public key formatress
# using pybitcointools (https://pypi.python.org/pypi/bitcoin) by vitalic
# 2018. 11. 4

# public key : (x, y) format
# uncompressed : 0x04 + x + y format
# compressed : (even) 0x02 + x, (odd) 0x0x + x format
# compressed ==> (x, y) converted

import bitcoin.main as btc

# generating private key (hex format)

while (1):
    privKey = btc.random_key()
    dPrivKey = btc.decode_privkey(privKey, 'hex')
    if dPrivKey < btc.N:
        break

print("\nprivate key (hex) : ", privKey)

# generating public key using Elliptic Curve Q = k*G
pubKey = btc.fast_multiply(btc.G, dPrivKey)

# print("\npublic key (x, y) format ==> \n", (%x, %y)(pubKey[0], pubKey[1]))

# generating uncomressed format. 0x04 + x + y format
uPubKey = btc.encode_pubkey(pubKey, 'hex')

print("\npublic key uncompressed format ==> \n: " ,uPubKey)
