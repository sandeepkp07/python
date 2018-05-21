import sys
def list(n):
	print "enter the string"
	a = [0 for i in range(n)]
	for i in range(n):
		a[i] = raw_input()
	count = 0
	for x in a:
		if len(x) >=2 and x[0] == x[-1]:
			count = count+1
	return count
a = input("enter the number of strings")
b = list(a)
print "no of strings is:",b
if __name__ == "__list__":
	list(n)
	
