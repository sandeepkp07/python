import sys
def enumerate_list(a):
 r = []
 k=len(a)
 for i in range(k):
  b=x[i]
  r.append((i,b))
 return r
n = int(input("enter the number of elements"))
print "enter elements"
x =[0 for i in range(n)]
for i in range(n):
 x[i] = raw_input()
print enumerate_list(x)
if __name__=="__enumerate_list__":
 enumerate_list(x)

