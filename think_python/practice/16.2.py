import sys
def is_after(t1,t2):
 return t1<t2

class time1(object):
 ""
clock = time1()
clock.hour = 11.00
clock.minute = 30.00
clock.sec = 07
class time2(object):
 ""
clock1 = time2()
clock1.hour = 12.00
clock1.minute = 30.00
clock1.sec = 07
print is_after(clock,clock1)


