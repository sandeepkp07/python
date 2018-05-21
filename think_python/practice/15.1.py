import math
def distance_points(p,q):
 a = p.x - q.x
 b = p.y - q.y
 distance = math.sqrt(a**2 + b**2)
 return distance
class point(object):
 ""
blank=point()
blank.x=3.0
blank.y=4.0
next=point()
next.x=5.0
next.y=6.0
print distance_points(blank,next)

