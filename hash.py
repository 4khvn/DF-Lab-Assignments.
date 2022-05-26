import hashlib
import uuid
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('device')
parser.add_argument('-b',type=int)
arg=parser.parse_args()
source=open(arg.device,'rb')
salt = "Anas"
hash_algo=hashlib.sha256()
while bytes:
	bytes=source.read(arg.b)
	hash_algo.update(bytes)
hash_algo.update(str.encode(salt))
hashed = hash_algo.hexdigest()
with open('hash.txt', 'w') as f:
    f.write(hashed)	
print(hashed)
source.close()

