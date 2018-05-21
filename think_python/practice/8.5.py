import sys
def count(w,l):
 count = 0
 for f in w:
  if f == l:
   count = count + 1
 return count
a = raw_input("enter string:\t")
b = raw_input("enter the letter to count repeatation:\t")
print count(a,b)
 

