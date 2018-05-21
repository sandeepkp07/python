import sys
a =int(input('enter the nomber'))
s = 0
t = a
while(a):
	r = a%10
	a = a/10
	s =s*10+r
if (s == t):
	print "palindrome"
else:
	print "not palindrome"

