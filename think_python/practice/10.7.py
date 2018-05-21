import sys
def anagrams(x,y):
 if x != y:
  if sorted(x) == sorted(y):
   print "true(real anagram)"
 else:
  print "not anagram"
a=raw_input("Enter first string")
b=raw_input("Enter second string")
anagrams(a,b)
