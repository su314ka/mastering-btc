# 2019/12/17 modified by WKIM using random_key(), random_electrum_seed() of \
# bitcoin-1.1.42\bitcoin\main.py


import time

entropy1 = time.time()
entropy2 = int(time.time())
entropy3 = str(int(time.time() * 1000000))

print("\n The result of time.time() ===> ", entropy1)
print("\n\n The result of int(time.time()) ===>", entropy2)
print("\n\n The result of str(time.time()) * 1000000 ===>", entropy3)

print("\n\n The program is ended\n")

input("\n\n\t\t if you wanna stop it, pls enter")
