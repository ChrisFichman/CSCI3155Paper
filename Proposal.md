Statically Nested Scope in Python.
==============================================

Authors:

Chris Fichman, Tony Gagliardi, Alec Martin

Introduction
------------

Specifications of the python programming language before version 2.2 did not allow for statically nested scopes, aka lexical scoping. That is, a function (f) which was defined inside the definition of function (g) could not reference names bound in (g). This limited the utility of nested function declarations, making functional style cumbersome to work with. Python Enhancement Proposal (PEP) 227, created 1 November 2000 by Jeremy Hylton [1][] adds this functionality to the python language. In this paper we will discuss how the community was involved in the design and final implementation of this PEP, as well as demonstrate the uses and implications of this addition to the Python language.

Specification
--------------
In the language definition for versions 2.0 and earlier of Python, exactly three namespaces were defined for resolving names; local, global and built-in. The addition of this particular PEP "allows resolution of unbound local names in enclosing functions' namespaces." This was mainly aimed at addressing two shortcomings found in Python at the time. The first being the limited utility of lambda expressions and nested functions in general. The second being the confusion from new users who came from other languages that supported nested lexical scopes/recursion. Since Python was originally designed to be purely a teaching language, it didn't make much sense for it to be missing attributes that are common in most other languages.

Discussion
--------------
An important thing to note right off the bat is that for code written in versions 2.0 and earlier, this addition may change particular functions' behavior, especially when dealing with recursion. Because of this, a warning will be issued at compile time for any code that may be affected by this.

The enclosed functions' namespace name resolution rules are similar to other languages, except for three major things.
One, names in class scope are not accessible (shown in more detail in example 3 below), two, the global statement short-circuits the normal rules, and three,  variables are not declared.

By making names in class scope not accessible, it prevents weird and inconsistent interactions between class attributes and local variable access. "If a name binding operation occurs in a class definition, it creates an attribute on the resulting class object." Therefore, an attribute reference must be used to access a function nested within a class via self or via the class name. Rule 2 is important because the global statement has the exact same effect as in Python 2.0 and earlier. Rule 3 is important because "if a name binding operation occurs anywhere in a function, then that name is treated as local to the function and all references refer to the local binding." As a consequence, it is not possible to rebind a name defined in an enclosing scope.

Tim Peters drew up an example that shows potential failures of nested scopes in the absence of declarations.

    i = 6
    def f(x):
        def g():
            print i
        # ...
		# move to next page
		# ...
        for i in x:  # ah, i *is* local to f, so this is what g sees
            pass
        g()

Here, function g() sees the variable i defined in the for loop by function f(). If g() is called before the loop is executed, a NameError will be raised.


Further Examples
--------------  
The following example is a lambda expression that yields an unnamed expression which evaluates a single expression.

    from Tkinter import *
      root = Tk()
      Button(root, text="Click here",
             command=lambda root=root: root.test.configure(text="..."))
Here, any name used in the body of the expression must be explicitly passed as an argument to the expression. This method can get very confusing in large scale implementations, almost to the point where the functions purpose cannot be understood from reading the code. This is exactly what this PEP was designed for, because it essentially implements this approach automatically by using the new enclosing functions' namespace.

The following example should look eerily familiar.

	>>> def make_adder(base):
    ...     def adder(x):
    ...         return base + x
    ...     return adder
    >>> add5 = make_adder(5)
    >>> add5(6)

This looks incredibly similar to most of the recursion functions we have been writing for our labs in this class. The PEP allows the expression "base" from function "make_adder" to be read by function "adder" via the enclosing functions' namespace.

Another example can be found when defining classes.

    >>> def make_wrapper(obj):
    ...     class Wrapper:
    ...         def __getattr__(self, attr):
    ...             if attr[0] != '_':
    ...                 return getattr(obj, attr)
    ...             else:
    ...                 raise AttributeError, attr
    ...     return Wrapper()
    >>> class Test:
    ...     public = 2
    ...     _private = 3
    >>> w = make_wrapper(Test())
    >>> w.public
    2
    >>> w._private
 
Names refer to objects in Python. In this example, the class definition for making a wrapper pulls in "obj" from the declaration found in function "make_wrapper", just like the previous example. Although, this example really illustrates the benefits found within this PEP, especially when it comes to class declarations.   

~~~~~~~~~~~
[1]: http://www.python.org/dev/peps/pep-0227/