import sys
def fact(n):
	if n<0:
		print "no factorial"
	else:
		s = 1
		for i in range(1,n+1):
			s = s*i
		print s
a = int(input('enter number'))
fact(a)
if __name__ =="__fact__":
	fact(n)
