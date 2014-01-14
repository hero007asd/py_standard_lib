'''
basic fifo queue
'''
import Queue
q1 = Queue.Queue()
for i in range(5):
	# print 'putting %d' % i
	q1.put(i)

while not q1.empty():
	print q1.get(),
print 

'''
LIFO Queue
'''
import Queue
q2 = Queue.LifoQueue()
for i in range(5):
	q2.put(i)
while not q2.empty():
	print q2.get(),
print 
'''
Priority Queue
'''
import Queue
import threading
class Job(object):
	def __init__(self,priority,description):
		self.priority = priority
		self.description = description
		print 'New Job:' , description
		return
	def __cmp__(self,other):
		return cmp(self.priority, other.priority)

q=Queue.PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(10,'Low-level job'))
q.put(Job(1,'Important job'))

def process_job(q):
	while True:
		next_job = q.get()
		print 'Processing job:',next_job.description
		q.task_done()
workers = [threading.Thread(target=process_job,args=(q,)),
			threading.Thread(target=process_job,args=(q,)),]
for w in workers:
	w.setDaemon(True)
	w.start()

q.join()

