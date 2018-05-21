import sys
def repdict(a):
 d = dict()
 for x in a:
  if x in d:
   return d[x]
  else:
   d[x] = 'True'
 return False
b=raw_input("enter string")
print repdict(b)
