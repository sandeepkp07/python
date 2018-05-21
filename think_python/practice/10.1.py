import sys
def nested_sum(x):
 return sum(int(i) for i in x)
a =raw_input("enter first list\t:")
a=list(a)
b =raw_input("enter second list\t:")
b=list(b)
c=a+b
print nested_sum(c)

