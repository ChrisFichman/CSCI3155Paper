# Statically Nested Scoping in Python #

Python Enhancement Proposal 227,
created by Jeremy Hylton, 1 November 2000

Alec Martin
Tony Gagliardi
Chris Fichman

# The "Ballmer Peak" #

- It really does exist!
- Remeber Windows ME?
- Jim does!

# What the  is Statically Nested Scoping? #

Let's start with an example:

	  def f(a):
	  	x = 42 + a
	  	def g(b):
	  		return b * x
	  	return g(a)

# The Unholy Age Before PEP 227 #

- Only 3 namespaces in python:
	1. Local.
	2. Global.
	3. Built-in.
- Lambdas must use arguments to create bindings in the surrounding namespace.
- Example on next slide...

# Beach (function) Body Before and After Pics #

Before:
	  def f(a):
	  	x = 42 + a
	  	def g(b, x):
	  		return b * x
	  	return g(a, x)

After:
	  def f(a):
	  	x = 42 + a
	  	def g(b):
	  		return b * x
	  	return g(a)

- Has nobody else noticed that "PEP 227" sounds like a sports drink?
- 400 babies!

# Inspiration for PEP 227 #

- Most modern languages use statically nested scoping for variables and functions.
- Statically nested scopin most associated with the ALGOL family of languages, including:
	- FORTRAN
	- Pascal
	- Lisp
	- C / C++
	- COBOL
- Python 