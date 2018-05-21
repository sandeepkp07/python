import sys
def is_sorted(x):
 n=0
 while n+1 < len(x):
   if x[n] <= x[n+1]:
     n = n + 1
   else:
    return "false"
 return "true"
n = int(input("Enter the number of elements\t:"))
print "Please enter the list\t:"
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input()
print is_sorted(a)

