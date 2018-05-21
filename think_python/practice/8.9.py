import sys
def reviter(x,y):
 p=[]
 if len(x) != len(y):
   return "cannot reverse"
 k=0
 i=0
 j=len(y) - 1
 while j >= 0: 
  if x[i] == y[j]:
   i=i+1
   j=j-1
   while k > i:
    p[k]=x[i]
    k=k+1
    print p,x
  else:
   return "nop"
a=raw_input("enter first word")
b=raw_input("enter second word")
print reviter(a,b)
 
