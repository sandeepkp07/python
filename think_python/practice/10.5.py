import sys
def chop(x):
 q = x[1:-1]
 print "modified list\t:",q
n = int(input("Enter the number of elements\t:"))
print "Please enter the elements\t:"
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input()
print chop(a)


