import urllib2
import os


url = "http://download.microsoft.com/download/a/0/9/a09e587c-4ff9-4a58-a854-56fe50b862b2/"

with open("target.txt",'r') as f:
	target = f.read().splitlines()

for t in target:
	if os.path.exists(t):
		print "%s already exists!" %t
	else:
		print "Download %s" %t
		filedata = urllib2.urlopen(url+t.replace(' ','%20'))  
		datatowrite = filedata.read()
		with open(t, 'wb') as f:  
			f.write(datatowrite)
		print "Complete"