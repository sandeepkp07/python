import sys
def nested_captlz(x):
 r = []
 for s in x:
  r.append(s.capitalize())
 return r
a =raw_input("enter first list\t:")
a=list(a)
b =raw_input("enter second list\t:")
b=list(b)
c=a+b
print nested_captlz(c)


