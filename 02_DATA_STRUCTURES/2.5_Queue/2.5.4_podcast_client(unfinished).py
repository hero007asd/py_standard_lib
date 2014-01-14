'''
building a threaded podcast client
'''
from Queue import Queue
from threading import Thread
import time
import urllib
import urlparse
import feedparser
# Set up some global variables
num_fetch_threads = 2
enclosure_queue = Queue()
# A real app wouldn't use hard-coded data..
feed_urls = ['http://advocacy.python.org/podcasts/littlebit.rss',]
def downloadEnclosures(i,q):
	"""This is the worker thread function.
	It processes items in the queue one after
	another.
	These daemon threads go into an
	infinite loop, and only exit when
	the main thread ends.
	"""
	while True:
		print '%s:Looking for the next enclosure' % i
		url = q.get()
		parsed_url = urlparse.urlparse(url)
		print '%s:Downloading' % i, parsed_url.path
		response = urllib.urlopen(url)
		data = response.read()
		# Save the downloaded file to the current director
		outfile_name = url.rpartition('/')[-1]
		with open(outfile_name,'wb') as outfile:
			outfile.write(data)
		q.task_done()

for i in range(num_fetch_threads):
	worker = Thread(target=downloadEnclosures,args=(i,enclosure_queue,))
	worker.setDaemon(True)
	worker.start()