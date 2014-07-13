#!/usr/bin/python

from os.path import exists


print "This is the program to copy one file to target file"

src = raw_input("enter source file> ")

if not exists(src):
	print "file does not exist"
	exit()


f1 = open(src)
data1 = f1.read()

f1.close()


dest = raw_input("enter target file> ")

if exists(dest):
	print "file exists..."
	exit()

f2 = open(dest, "w")

f2.write(data1)

f2.close()




