import sys
class Time(object):
 "racing"
def mul_time(t1,f):
 t1 = valid_time(t1)
 second = time_to_int(t1) * f
 return int_to_time(second)


def valid_time(s):
 if s.hour < 0 or s.minute < 0 or s.sec < 0:
  return False
 if s.minute >= 60 or s.sec >= 60:
  return False
 return s


def int_to_time(secnds):
 time = Time()
 minutes, time.sec = divmod(secnds, 60)
 time.hour, time.minute = divmod(minutes, 60)
 s = '%.2d:%.2d:%.2d' % (time.hour,time.minute,time.sec)
 return s

def time_to_int(time):
 minutes = time.hour * 60 + time.minute
 secnds = minutes * 60 + time.sec
 return secnds


str = Time()
str.hour = 1.00
str.minute = 25.00
str.sec = 00
distance = 2.1
print mul_time(str,1/distance)
