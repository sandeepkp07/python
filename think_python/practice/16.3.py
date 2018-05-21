import sys
def add_time(t1,t2):
 t1 = valid_time(t1)
 t2 = valid_time(t2)
 class Time(object):
  "sum of t1 and t2"
 sum = Time()
 sum.hour = start.hour + dur.hour
 sum.minute = start.minute + dur.minute
 sum.sec = start.sec + dur.sec
 return '%.2d:%.2d:%.2d' % (sum.hour,sum.minute,sum.sec)

def valid_time(s):
 if s.hour < 0 or s.minute < 0 or s.sec < 0:
  return False
 if s.minute >= 60 or s.sec >= 60:
  return False
 return s

class time1(object):
 ""
start = time1()
start.hour = 10.00
start.minute = 30.00
start.sec = 07
dur = time1()
dur.hour = 1.00
dur.minute = 25.00
dur.sec = 00
print add_time(start,dur)


