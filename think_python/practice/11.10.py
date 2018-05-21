import sys
def rotatefl(x):
 d = dict()
 for f in x:
  for i in range(1,14):
   p = f[-i:] + f[:-i]
   if p not in d:
    if p!=f:
     if p in x:
      d[f] = p
      print d,"rotated\t:",i
b = []
for f in open('rot.txt'):
 c = f.strip().lower()
 b.append(c)
print rotatefl(b)
