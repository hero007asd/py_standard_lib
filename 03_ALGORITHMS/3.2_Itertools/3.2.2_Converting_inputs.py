from itertools import *
print 'Doubles:'
for i in imap(lambda x:x*2,xrange(5)):
	print  i
print 'multiplies:'
for i in imap(lambda x,y:(x,y,x*y),xrange(5),xrange(5,10)):
	print i
	print '%d * %d = %d' % i
print '================================='
for i in [(0,4,3),(0,4,5)]:
	print '%d + %d = %d' % i

print '================================='
values = [(0,5),(1,6),(2,7),(3,8),(4,9)]
for i in starmap(lambda x,y:(x,y,x*y),values):
	print '%d * %d = %d' % i

