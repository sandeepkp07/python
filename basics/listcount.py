import sys
print "enter word"
s = raw_input()
s = list(s)
b = ['a','e','i','o','u']
count = 0
t = 0
for f in s:
	if f in b:
		count = count+1
	else:
		t = t+1
print "consonenets number:",t
print "vowels number:",count


