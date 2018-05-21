import sys
def dictsrch(x):
 y=[]
 a=dict()
 index=1
 for f in x:
  y.append(f)
 for s in y:
  a[index]=s
  index=index+1
 print a.keys()
i=open('word.txt')
dictsrch(i)
