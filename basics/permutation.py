import sys
def permutation(x, y):
 if len(x)==len(y):
   c= sorted(x)
   d= sorted(y)
   if c==d: 
    print "true\n"
   else:
    print "false\n"

a = raw_input("enter first string\t")
b = raw_input("enter second string\t")
print permutation(a,b)
if __name__=="__permutation__":
 permutation(a,b)


