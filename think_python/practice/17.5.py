import sys
class Addition(object):
 def __init__(self,x,y):
  self.x = x
  self.y = y
 def __str__(self):
  return str(c)
def add(self):
  if type(self.x) == int:
   c=self.x+self.y
   return c
  else:
   if type(self.x) == tuple:
    c=self.x[0]+self.y[0],self.x[1]+self.y[1]
    return c
   else:
    return "error"

s=Addition(1,2)
c = add(s)
print c

