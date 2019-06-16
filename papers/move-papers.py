#!/usr/bin/python

from os import listdir, renames, symlink

for file in listdir("."):
	if file.endswith(".pdf"):
		year = file[-8:-4]
		if year.isdigit():
			print "%s => %s" % (file, year + "/" + file)
			renames(file, year + "/" + file)
			symlink(year + "/" + file, file)
