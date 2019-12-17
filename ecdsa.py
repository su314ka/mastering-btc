# package : pybitcointools (https://pypi.python.org/pypi/bitcoin written by vitalik
# ECDSA Test by wkim, 2018. 10. 21

import bitcoin.main as btc

d=btc.random_key()
Q=btc.privkey_to_pubkey(d)
G=btc.getG()
Gx=int(G[0])
print("\n ===Private Key(d)=== \n", d, "\n ===PrivKey Length(byte)===", len(d))
print("\n ===Generator x, y ===", len(G), "\n Generator(G)=== \n", G)
print("\t ===G[0] == \t", G[0])
print("\t ===Gx == \t", Gx)

print("\n\t ===Gy == \t", G[1])

print("\n ===Public Key Q=d*G=== \n", Q,"\n ===Pubkey Len(byte)===", len(Q))

message="This message is the original document for testing ECDSA."

en_m=message.encode()
#print("\n ===The result of encoding the input document===\n", en_m)

v,r,s=btc.ecdsa_raw_sign(btc.electrum_sig_hash(en_m),d)
print("\n ===ECDSA raw Signature Result(v)=== \n", v)
print("\n ===ECDSA raw Signature Result(r)=== \n", r)
print("\n ===ECDSA Signature Result(s)=== \n", s)

sig1=btc.encode_sig(v,r,s)
print("\n===Signature Result(sig1)===\n", sig1)

sig2=btc.ecdsa_sign(en_m,d)
print("\n ===Signature Result(sig2)=== \n", sig2)

v=btc.ecdsa_verify(en_m,sig2,Q)
print("\n===v's value===\t", v)

print("\nMessage =", en_m.decode())
if v:
    print("\n Valid Signature")
else:
    print("\n Invalid Signature") 


#passphrase = 'Brain wallet\'s test private key. forget it'
#privKey = btc.sha256(passphrase)
#dprivkey = btc.decode_privkey(privKey, 'hex')

#print("\n === PassPhrase ====\n", passphrase) 
#print("\n === privKey ====\n", privKey) 
#print("\n === decimal of privkey ====\n", dprivkey) 

input("\n\n\t\t if you wanna stop it, pls enter")

