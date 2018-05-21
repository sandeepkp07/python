import sys
def interlock(x,y):
 p=0
 q=0
 z=[]
 for i in x:
  z.append(i)
  for j in y[q:]:
   if p == 0:
    z.append(j)
    p = p + 1
  p = p - 1
  q = q + 1
 print ''.join(z)
a = raw_input("Enter first word")
b = raw_input("Enter second word")
print interlock(a,b)
