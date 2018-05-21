z=[]
import sys
def perms(x, y):
        for f in y:
         if len(f)==len(x):
		c=sorted(f)
		d=sorted(x)
		if c==d:
		 z.append(f)
        
        return z
a=raw_input("enter the initial string\t")
n=int(input("number of strings to be checked\t"))
b=[0 for i in range(n)]
for i in range(n):
 b[i]=raw_input("enter the list of strings\t")
print perms(a,b)
if __name__=="__perms__":
 perms(a,b)


 	 
