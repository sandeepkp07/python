import sys
def middle(x):
 q = x[1:-1]
 return q
n = int(input("Enter the number of elements\t:"))
print "Please enter the elements\t:"
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input()
print middle(a)


