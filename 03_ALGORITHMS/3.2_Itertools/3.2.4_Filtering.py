from itertools import *
def should_loop(x):
	print 'Testing:',x
	return (x<1)
for i in dropwhile(should_loop,[-1,0,1,2,-2]):
	print 'Yielding:',i,
print 
print '========================================'
def should_take(x):
	print 'Testing:',x
	return (x<2)
for i in takewhile(should_take,[-1,0,1,2,-2]):
	print 'Yielding:',i,
print 
print '================like built-in filter()========================'
def check_item(x):
	print 'Testing:',x
	return (x<1)
for i in ifilter(check_item,[-1,0,1,2,-2]):
	print 'Yielding:',i
print 
print '======================================='
for i in ifilterfalse(check_item,[-1,0,1,2,-2]):
	print 'Yielding:',i

