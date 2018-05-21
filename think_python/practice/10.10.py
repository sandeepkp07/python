import sys
def flist(x):
 b = []
 for f in open(x):
  b = b + [f]
 print b
flist('abc.txt')
