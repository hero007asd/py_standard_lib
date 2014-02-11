from itertools import *
for i in izip(count(1),['a','b','c']):
	print i
print '==========count & xrange &range============='
for i,item in izip(xrange(7),cycle(['a','b','c'])):
	print (i,item)
print '==========cycle============='
for i in repeat('over-and-over',5):
	print i 
print '==========repeat============='

for i,s,c in izip(count(),repeat('over-and-voer',5),cycle([1,2])):
	print i,s,c

print '==========izip count repeat cycle============='
for i in imap(lambda x,y:(x,y,x*y),repeat(2),xrange(5)):
	print '%d * %d = %d' % i