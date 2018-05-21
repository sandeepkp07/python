import sys
class point(object):
 def __str__(self):
  return '(%d,%d)' % (self.x,self.y)
par=point()
par.x = 4
par.y = 3
print par
