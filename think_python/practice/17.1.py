import sys
class Time(object):
 def conv(self):
  self = self.time_to_int()
  print self
 def time_to_int(s):
  minutes = s.hour * 60 + s.minute
  secnds = minutes * 60 + s.sec
  return secnds

start = Time()
start.hour = 11.00
start.minute = 30.00
start.sec = 07
start.conv()

