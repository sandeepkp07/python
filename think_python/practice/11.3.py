import sys
def orderhist(h):
 b = sorted(h.keys())
 for t in b:
  print t,h[t]
a = raw_input("enter:\t")
d = dict()
for c in a:
 if c not in d:
  d[c] = 1
 else:
  d[c] += 1
orderhist(d)

