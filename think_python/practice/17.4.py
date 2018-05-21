import sys
class point(object):
 def __str__(self):
  self = self.add()
  return 'sum:%d' % (self)
 def add(x):
  c= x.x + x.y
  return c
par=point()
par.x = int(input("enter the x coordinate value:"))
par.y = int(input("enter the y coordinate value:"))
print par



