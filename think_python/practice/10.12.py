import sys
def revwords(x):
 rev=""
 list=x
 for w in list:
  w=w in list
  rev=rev+w+""
 return rev
n = int(input("enter count:"))
a = [0 for i in range(n)]
print "common:\t"
for i in range(n):
 a[i] = raw_input()
revwords(a)
