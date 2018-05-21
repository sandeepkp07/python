import sys
def hist_get(x):
 y = dict()
 for f in x:
  c = y.get(f,0)
  c = c + 1
  y[f] = c 
 print y
a = raw_input("Enter your string:  ")
b = list(a)
hist_get(b)
