from itertools import *
for i in chain([1,2,3],['a','b','c']):
	print i,
print 
print '=============================='
for i in izip([1,2,3],['a','b','c']):
	print i
print '=============================='
print 'Stop at 5:'
for i in islice(count(),5):
	print i,
print '\n'
print 'Start at 5,Stop at 10:'
for i in islice(count(),5,10):
	print i,
print '\n'
print 'By tens to 100:'
for i in islice(count(),0,100,10):
	print i,
print 
print '=============================='

r = islice(count(),5)
i1,i2=tee(r)
print 'i1:',list(i1)
print 'i2:',list(i2)
print '=============================='
r = islice(count(),5)
i1,i2=tee(r)
for i in r:
	print i,
	if i>1:
		break
print 'i1:',list(i1)
print 'i2:',list(i2)