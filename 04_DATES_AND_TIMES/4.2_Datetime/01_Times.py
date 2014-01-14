import datetime
t  = datetime.time(1,2,3)
print t
print 'hour    :',t.hour
print 'minu    :',t.minute
print 'seco    :',t.second
print 'microse :',t.microsecond
print 'tzinfo  :',t.tzinfo
#####################################
print 'earliest   :',datetime.time.min
print 'latest     :',datetime.time.max
print 'resolution :',datetime.time.resolution
#######################################
for m in [1,0,0.1,0.6]:
	try:
		print '%02.1f:' % m,datetime.time(0,0,0,microsecond=m)
	except TypeError,err:
		print 'ERROR:',err