import sys
def rotstr(x,y):
 print x[-y:] + x[:-y]
a=raw_input("Enter string")
b=int(input("needed number of rotations"))
print rotstr(a,b)
