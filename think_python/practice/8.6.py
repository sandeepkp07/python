import sys
def find(w,l,i):
 index = i
 count = 0
 while index < len(w):
  if w[index] == l:
   count = count + 1
  index= index + 1
 return count
a=raw_input("enter the word\t:")
b=raw_input("enter the letter\t:")
c=int(input("from:"))
print find(a,b,c)
if __name__ == "__find__":
 find(a,b,c)

