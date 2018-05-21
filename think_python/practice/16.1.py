import sys
def print_time(time):
 return '%.2d:%.2d:%.2d' % (time.hour,time.minute,time.sec)
class time(object):
 "display time"
clock = time()
clock.hour = 11.00
clock.minute = 30.00
clock.sec = 07
print print_time(clock)


