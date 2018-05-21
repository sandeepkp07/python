import sys
def find(w,l,i):
 index = i
 while index < len(w):
  if w[index] == l:
   print index
  index= index + 1
a=raw_input("enter the word\t:")
b=raw_input("enter the letter\t:")
c=int(input("from:"))
print find(a,b,c)
