import sys
class time(object):
 def __cmp__(t1,t2):
  if t1.hour > t2.hour:return 1
  if t1.hour < t2.hour:return -1
  if t1.hour == t2.hour:
   if t1.minute > t2.minute:return 1
   if t1.minute < t2.minute:return -1
   if t1.minute == t2.minute:
    if t1.sec > t2.sec:return 1
    if t1.sec < t2.sec:return -1
    if t1.sec == t2.sec:print "same time"
self = time()
self.hour=int(input("Enter the first time parameters:\n\tEnter hour:"))
self.minute=int(input("\tEnter min:"))
self.sec=int(input("\tEnter sec:"))
other = time()
other.hour=int(input("Enter the second time parameters:\n\tEnter hour:"))
other.minute=int(input("\tEnter minute:"))
other.sec=int(input("\tEnter sec:"))
print time.__cmp__(self,other)

