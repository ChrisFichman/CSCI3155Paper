# Statically Nested Scoping in Python #

Python Enhancement Proposal 227,
created by Jeremy Hylton, 1 November 2000

Alec Martin
Tony Gagliardi
Chris Fichman

# The "Ballmer Peak" #

- It really does exist!
- Remeber Windows ME?

# What is Statically Nested Scoping? #

Let's start with an example:

  def f(a):
  	x = 42 + a
  	def g(b):
  		return b * x
  	return g(a)

# Why statically nested scoping? #

- Allows for functional style
