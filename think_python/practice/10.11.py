import sys
def indexlist(x,y):
 b = []
 if y not in x:
  print "nop"
 else:
  for f in x:
   if f == y:
    b.append(str(x.index(f)))
    print b
a = []
a = raw_input("Enter string")
v = raw_input("Enter element to be searched:")
print indexlist(a,v)
