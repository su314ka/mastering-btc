# private key & public key, public key -> wallet address
# using pybitcointools (https://pypi.python.org/pypi/bitcoin) by vitalic
# 2018. 11. 3

import bitcoin.main as btc

while (1):
    privKey = btc.random_key()
    dPrivKey = btc.decode_privkey(privKey, 'hex')
    if dPrivKey < btc.N:
        break

# generating from private key to public key 
pubKey = btc.privkey_to_pubkey(privKey)

# from public key to Mainnet wallet address (prefix : 0x00)
address1 = btc.pubkey_to_address(pubKey, 0x00)

# public key => 160bit public key hash
pubHash160 = btc.hash160(btc.encode_pubkey(pubKey, 'bin'))

# 160 bit public key hash => wallet address
address2 = btc.hex_to_b58check(pubHash160, 0x00)

# public key => Testnet wallet address (prefix : 0x6f)
address3 = btc.pubkey_to_address(pubKey, 0x6f)

print("\nPrivate key : ", privKey)
print("\nPublic key : ", pubKey)
print("\nprefix 0x00 Mainnet wallet address : ", address1)


print("\nPublickey => 160bit hash : ", pubHash160)
print("\nMainnet wallet address : ", address2)
print("\nTestnet address 0x6f : ", address3)


input("\n\n\t\t if you wanna stop it, pls enter")

