Lightning Talk: CSCI3155
-----------------------------------------------------------

Statically Nested 
Scope in Python:
-----------------------------------------------

Presentation by: Chris Fichman, 


Tony Gagliardi, and Alec Martin

Problems with Python Prior to Version 2.2
-----------------------------------------------------------
  - Python does not allow nested scopes(also known as lexical scoping)
  - This means that a function `f` defined within function <g> could not 
  reference names bound in `g`, which code like the following is 
  not possible:
  
	
		def f(x):
			x = 5
			def g(y):
				y = 3
				x = y
				return y
			return x
			
PEP 227
-----------------------------------------------------------
  - Proposed 1 November 2000 by Jeremy Hylton
  - Adds Nested Scoping
  - Initially Deferred
