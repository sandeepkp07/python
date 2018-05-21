import sys
def repeats(x):
 y=[]
 for f in x:
  if f not in y:
   y.append(f)
  else:
   return "repeats"
 return "not repeats"
a=raw_input("enter string:")
print repeats(a)
