import hashlib
import time
#Data to use to calculate md5 checksums
# data = open(__file__,'rt').read()

# for i in range(5):
# 	h = hashlib.sha1()
# 	print time.ctime(),':%0.3f %0.3f' %  (time.time(),time.clock())
# 	for i in range(300000):
# 		h.update(data)
# 	cksum = h.digest()

for i in range(6,1,-1):
	print '%s %0.2f %0.2f' % (time.ctime(),time.time(),time.clock())
	print 'sleeping',i
	time.sleep(i)