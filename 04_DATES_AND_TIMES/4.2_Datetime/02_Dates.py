import datetime
today = datetime.date.today()
print today
print 'ctime  :',today.ctime()
tt = today.timetuple()
print tt.tm_year
print tt.tm_mon
print tt.tm_mday
print tt.tm_hour
print tt.tm_min
print tt.tm_sec
print tt.tm_wday
print tt.tm_yday
print tt.tm_isdst
print today.toordinal()
print today.year
print today.month
print today.day
print('==========================================================')
import time
o=733114
print 'o             :',o
print 'fromordinal(o):',datetime.date.fromordinal(o)
t = time.time()
print 't             :',t
print 'fromtimestamp(t):',datetime.date.fromtimestamp(t)
print('==========================================================')

print 'earliest   :',datetime.date.min
print 'latest     :',datetime.date.max
print 'resolution :',datetime.date.resolution
print('==========================================================')

d1 = datetime.date(2008,1,28)
print d1.ctime()
d2 = d1.replace(year=2014)
print d2.ctime()