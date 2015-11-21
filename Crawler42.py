import urllib
from Queue import *
import time

"""
My Beacon number is 2.

A crawler by Aditya Vinayak Chaturvedi
"""
timeInterval = 10

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

startTime = time.time()
lastTime = int((time.time()-startTime)/timeInterval)

if "wikipedia" not in url1 or "wikipedia" not in url2:
	print "Incorrect URL"
	exit(0)

try:
	handle = urllib.urlopen(url1).read()
except IOError:
	print "Incorrect URL"
	exit(0)

stuff = handle.split()

q = Queue()
link1 = linkDist(url1, 0)
q.put(link1)
lastDist = 0

while not q.empty():
	if int((time.time()-startTime)/timeInterval)!=lastTime:
		lastTime = int((time.time()-startTime)/timeInterval)
		print str(lastTime*timeInterval) + " seconds elapsed since starting."
	linkDistNow = q.get()
	disNow = linkDistNow.getDis()
	if int(disNow) != int(lastDist):
		print "Exploring at depth: " + str(disNow)
		lastDist = disNow
	if int(disNow) > int(maxDistance):
		print "No connection found within max distance."
		break
	if linkDistNow.getLink().lower()==url2.lower():
		print "True: " + str(disNow) + " away."
		break
	handle = urllib.urlopen(linkDistNow.getLink()).read().split()
	for i in handle:
		if "href=\"/wiki/" in i and ":" not in i:
			newurl = "https://en.wikipedia.org" + i[6:-1]
			tempLink = linkDist(newurl, disNow+1)
			q.put(tempLink)