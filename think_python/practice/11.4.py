import sys
def rev_look(x):
 z=[]
 v=int(input("enter value\t:"))
 for k in x:
  if d[k] == v:
   z.append(k)
 return z
d=dict()
a= raw_input("enter:")
for c in a:
 if c not in d:
  d[c] = 1
 else:
  d[c] += 1
print rev_look(d)
