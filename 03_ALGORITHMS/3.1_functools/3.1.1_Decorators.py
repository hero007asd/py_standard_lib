# -*- coding: UTF-8 -*-
import functools
def myfunc(a,b=2):
	print '   called myfunc with:',(a,b)
	return 

def show_details(name,f,is_partial=False):
	print '%s:' % name
	print '   object:',f
	if not is_partial:
		print '  __name__:',f.__name__
	if is_partial:
		print '    func:',f.func
		print '    args:',f.args
		print '    keywords:',f.keywords

show_details('myfunc', myfunc)
myfunc('a',3)
print '================================================='
# Set a different default value for ’b’, but require
# the caller to provide ’a’
p1 = functools.partial(myfunc,b=4)
show_details('partial with name default', p1,True)
p1('passing a')
p1('passing b',b=5)
print '================================================='
# Set default values for both ’a’ and ’b’.
p2=functools.partial(myfunc,'default a',b=99) 
show_details('partial with default', p2,True)
p2()
p2(b='override b')
print 
print 'Insufficient arguments:'
p1()
