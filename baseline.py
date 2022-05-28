import os
import hashlib
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('dir1',help='path of 1st directory')
parser.add_argument('dir2',help='path of 2nd directory')
args = parser.parse_args()
directory1 = args.dir1
directory2 = args.dir2
x=0
y=0
check=1
i=0
for root, dirs, files in os.walk(directory1):
    for filename in files:
        f = os.path.join(root, filename)
        if os.path.isfile(f):
            x+=1
for root, dirs, files in os.walk(directory1):
    for filename in files:
        f = os.path.join(root, filename)
        if os.path.isfile(f):
            y+=1
if x != y:
   print("Not Same")
   print("Directory 1 files",x)
   print("Directory 2 files",y)
else:
    p = None
    q = None
    r = None
    s = None
    for root, dirs, files in os.walk(directory1):
        for filename in files:
           i+=1
           j=0
           hash_algo=hashlib.sha256()
           f = os.path.join(directory1, filename)
           if os.path.isfile(f):
               p = open(f,'rb').read()
               hash_algo.update(p)
               q = hash_algo.hexdigest()
           for root, dirs, files in os.walk(directory1):
               for filename in files:
                   j+=1
                   hash_algo=hashlib.sha256()
                   u = os.path.join(directory2, filename1)
                   if os.path.isfile(u):
                       r = open(u,'rb').read()
                       hash_algo.update(r)
                       s = hash_algo.hexdigest()
                   if s == q:
                       check+=1
                       continue
                   elif j == y:
                           if check == 1:
                               print(filename,"Not present in other directory")
                               break
                           if check == x:
                               print("Same")
                               break
                   
                   
