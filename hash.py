import hashlib
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('device')
parser.add_argument('-b',type=int)
arg=parser.parse_args()
source=open(arg.device,'rb')
hash_algo=hashlib.sha256()
while bytes:
	bytes=source.read(arg.b)
	hash_algo.update(bytes)
with open('hash.txt', 'w') as f:
    f.write(hash_algo.hexdigest())	
print(hash_algo.hexdigest())
source.close()

