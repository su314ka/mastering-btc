# Vanity wallet
# using pybitcointools (https://pypi.python.org/pypi/bitcoin) by vitalic
# 2018. 11. 3

import bitcoin.main as btc

#bFound = False
#for i in range(100):
while (1):
    privKey = btc.random_key()
    pubKey = btc.privkey_to_pubkey(privKey)
    address1 = btc.pubkey_to_address(pubKey, 0x00)
    print("\nwallet address :\n ", address1, len(privKey))
    print("\nwallet address[0-3] : \n", address1[0:3])
    if address1[0:3] == '1KW':
        break

print("\nPrivate Key : \n", privKey)
print("\nPublic Key : \n", pubKey)
print("\nWallet Address is starting from 1KW")
print("\nwallet address : \n", address1)

input("\n\n\t\t if you wanna stop it, pls enter")
