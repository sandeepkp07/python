import sys
class Time(object):
 ""
def add_time(t1,t2):
 t1 = valid_time(t1)
 t2 = valid_time(t2)
 seconds = time_to_int(t1) + time_to_int(t2)
 return int_to_time(seconds)


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


start = Time()
start.hour = 10.00
start.minute = 30.00
start.sec = 07
dur = Time()
dur.hour = 1.00
dur.minute = 25.00
dur.sec = 00
print add_time(start,dur)



