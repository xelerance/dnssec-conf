#!/usr/bin/python

import re
import os

kf = "ripe-ncc-dnssec-keys-new.txt"
fp = open(kf,"r")
zname = ""
second = 0

for line in fp.readlines():

	# skip header
	if not zname:
		if not "arpa" in line:
			continue

	line = line.strip()

	if "arpa" in line:
		line = "%s "%line
		try:
			if zname:
				if not second:
					fz.write("\n\n};\n")
				fz.close()
		except:
			pass
		zname = line.split('"')[1]
		if os.path.isfile("/tmp/r/%sconf"%zname):
			fz = open("/tmp/r/%sconf"%zname,"a")
			second = 1
		else:
			fz = open("/tmp/r/%sconf"%zname,"w")
			second = 0
		if not second:
			fz.write("//; https://www.ripe.net/projects/disi//keys/ripe-ncc-dnssec-keys-new.txt\n//; 2010-03-23\ntrusted-keys {\n")
		fz.write(line)
	else:
		line = re.sub("Key ID=","key id =",line)
		line = re.sub(";","; ",line)
		try:
			if line[-1] == "\n":
				line = line[:-1]
		except:
			pass
		fz.write(line)


