#! /usr/bin/python

x = 22
def g():
	x = 44
	def f():
		print x
	return f()
g()