import sys
def sumall(x):
 c = sum(x)
 print c
a= int(input("enter limit"))
b =[0 for i in range(a)]
for i in range(a):
 b[i]=int(input("enter num\t:"))
f=tuple(b)
sumall(f)
