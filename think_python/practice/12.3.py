import sys
def mst_freq(x):
 d = dict()
 t=[]
 res=[]
 for c in x:
  if c not in d:
   d[c] = 1
  else:
   d[c] += 1
 for x, freq in d.iteritems():
     t.append((freq, x))
 t.sort(reverse=True)
 for u in t:
  print u
a=raw_input("enter the string")
print mst_freq(a)
