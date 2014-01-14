import datetime
print 'Now   :',datetime.datetime.now()
print 'TOday :',datetime.datetime.today()
print 'UTC Now:',datetime.datetime.utcnow()
print 

FIELDS = ['year','month','day','hour','minute','second','microsecond']
d= datetime.datetime.now()
for attr in FIELDS:
	print '%15s: %s' % (attr,getattr(d, attr))

print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
t = datetime.time(1,2,3)
print 't  :',t
d = datetime.date.today()
print 'd  :',d
dt = datetime.datetime.combine(d,t)
print 'dt  :',dt