#!/usr/python
import glob as gl
# This is a hello world program.
print "Hello World"
print "My name is Evans"
# Working with list of files
CUR_DIR='/Users/evans/Desktop/aims_gh-research-project'
# Printing all files in a the current directory
ALL_FILES gl.glob("*.*")
for f in ALL_FILES:
	print f
