import sys
def inverse(d):
 inverse = dict()
 for key in d:
  val = d[key]
  if val not in inverse:
   inverse[val] = key
  else:
   inverse[val].append(key)
 return inverse
n= int(input("enter the num of elements:\t"))
print "enter elements:\t"
x = [0 for i in range(n)]
for i in range(n):
 x[i] = raw_input()
y = dict()
index = 1
for f in x:
 y[f] = index
 index = index+1
print y
print inverse(y)
if __name__=="__inverse__":
 inverse(y)

 
