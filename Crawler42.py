"""
This is the answer to the ultimate question of Life, the Universe and Everything.

A crawler by Aditya Vinayak Chaturvedi.

View README for details on implementation.
"""

import urllib
from Queue import *
import time

# Assign the time interval to print how much time has passed.
timeInterval = 10

# Wrapper class to add to queue
class linkDist:
	def __init__(self, link, dis):
		self.link = link
		self.dis = dis
	def getDis(self):
		return self.dis
	def getLink(self):
		return self.link

# Take input for links to be connected and the max distance; initializes counter to zero.
url1 = raw_input('Enter the first Wikipedia link: ')
url2 = raw_input('Enter the second Wikipedia link: ')
maxDistance = raw_input('Enter maximum connection distance: ')

# Initialize timer.
startTime = time.time()
lastTime = int((time.time()-startTime)/timeInterval)

# A few security checks.
if "wikipedia" not in url1 or "wikipedia" not in url2:
	print "Incorrect URL"
	exit(0)

try:
	handle = urllib.urlopen(url1).read()
except IOError:
	print "Incorrect URL"
	exit(0)

# Initialize Queue.
q = Queue()
link1 = linkDist(url1, 0)
q.put(link1)
lastDist = -1

while not q.empty():
	# Display the time elapsed.
	if int((time.time()-startTime)/timeInterval)!=lastTime:
		lastTime = int((time.time()-startTime)/timeInterval)
		print str(lastTime*timeInterval) + " seconds elapsed since starting."
	# Explore the next element in the queue.
	linkDistNow = q.get()
	disNow = linkDistNow.getDis()
	print linkDistNow.getLink() + " : " + str(disNow)
	if int(disNow) != int(lastDist):
		print "Exploring at depth: " + str(disNow)
		lastDist = disNow
	# Check for required url.
	if linkDistNow.getLink().lower()==url2.lower():
		print "True: " + str(disNow) + " away."
		exit(0)
	# Do not add elements to queue if already at max distance.
	if int(disNow) >= int(maxDistance):
		print "here"
		continue
	# Add all links from this page to queue.
	handle = urllib.urlopen(linkDistNow.getLink()).read().split()
	for i in handle:
		if "href=\"/wiki/" in i and ":" not in i:
			newurl = "https://en.wikipedia.org" + i[6:-1]
			tempLink = linkDist(newurl, disNow+1)
			q.put(tempLink)
print "No connection found within max distance."
