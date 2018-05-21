import sys
def linecount(x):
 count=1
 for line in open(x):
  count += 1
 return count
print linecount('wc.py')
if __name__ == '__main__':
 print linecount('wc.py')
