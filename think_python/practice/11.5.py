import sys
def invert_dict(x):
 y=x.keys()
 inverse=dict()
 for k in x:
  if d[k] not in inverse:
   inverse[d[k]] = [k]
  else:
   inverse[d[k]].append(k)
   inverse.setdefault(x[k],y)
 return inverse
d=dict()
a= raw_input("enter:")
for c in a:
 if c not in d:
  d[c] = 1
 else:
  d[c] += 1
print invert_dict(d)

