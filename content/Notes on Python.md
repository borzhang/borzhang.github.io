Title: Notes on Python
Date: 20161006
tags: python

Ah, I love python. Oh no, it's Python. Here's a memo just for myself, it's quite conceptional, not just a copy from document. It will be updated at any time. 

* __What does it mean by "built-in" modules and names?__

	It's with respect to the interpreter. Those modules built into the interpreter are built-in modules. When you start an interpreter, using the interactive environment in the command line or an IDE like Pycharm or whatever ways else, those modules are already there. If you check all names your current module already defines by using `dir()`, you probably get a result like 

		['__builtins__', '__doc__', '__name__', '__package__']
That means some actions are done when the interpreter starts. Here the value of the name `__builtins__` is usually the standard module `__builtin__`. So if you further check all names defined in this module using `dir(__builtins__)`, you'll get a bunch of names like follows:

		['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
Notice that this whole series of modules are already built in your interpreter, you can use or check them directly specifying their names without importing. 

	But what's a bit funny is that the module `__builtin__` itself is not a built-in module. The value of the built-in variable `__builtins__` is this module. 

* __What is the list of paths used for the interpreter to search for modules?__

	The variable `sys.path`. It's initialized with the environment variable `PYTHONPATH` or a built-in default. Its type is python list. 

* __How to check linear algebra library linked in numpy?__

	There's [a question on stackoverflow](http://stackoverflow.com/questions/9000164/how-to-check-blas-lapack-linkage-in-numpy-scipy), see the most voted answer, which is not the accepted one.

		>>> import numpy as np
		>>> np.__config__.show()

* __What is metaclass?__

	There's [a perfect answer on stackoverflow](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python), see the most voted but not accepted one. But there's an even better [article](https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/). 

	In short, `class` (here we assume old-style class is gone from python, we will never use it) is a class, `type` is also a class, and classes are all objects in python. When representing a noun, the word `class` is usually used for user-defined classes, and `type` for built-in classes. 

	`type(yourobject)` is not a function but a class creator. However it often acts as a function. It creates an "type" object (a class), which is the type of this object. `type(name, bases, dict)` returns a new "type" object (a class), it's actually a dynamic form of the `class` statement. So in the second way, `type` creates a class object, just as `class` statement does. What creates class objects is called __metaclass__. `type` is the default metaclass used by python. You can set your metaclass to replace `type` to create a class, by putting `__metaclass__=yourmetaclass` under `class Yourclass(baseclass):` statement. 

	Roughly speaking, `thisobject.__class__` attribute is just "who creates this object". If `thisobject` is a class, then the value of `thisobject.__class__` is the metaclass who created it, usually `type`. 

* __What is proxy object?__

	Refer to this excellent [article](http://mindtrove.info/python-weak-references/), and the [document](https://docs.python.org/2/library/weakref.html?highlight=proxy#weakref.proxy). In short, a proxy object can be used just like a strong reference of an object, say if `a = Foo(); b = weakref.proxy(a)`, then you can just use `b` like `a`, `b` is an alternative of `a`. When `a` is deleted, for example by `del a`, then that object is deleted, and further using of `b` will raise exceptions. 

	If `b = weakref.ref(a)`, then `b` is a weak reference, which is a callable. We retrieve the pointed object by calling it: `b()`. When `a` is deleted, then calling `b()` will get `None` without any exception. 

* __What is closure?__
	
	Refer to this [article](http://www.shutupandship.com/2012/01/python-closures-explained.html). I'd like to just put the summary in that article here, because it's brief and clear enough:

	* Closure is just a fancy name for a function that remembers the values from the enclosing lexical scope even when the program flow is no longer in the enclosing scope.
	* If you've ever written a function that returned another function, you may have used closures. 
	
	So there's nothing deep or mysterious. `func.__closure__` is a tuple including details of the variables defined in the enclosing scope, one can access the content of those variables using `func.__closure__[i].cell_contents`. 

* __What is "method"?__

	Refer to this [question](http://stackoverflow.com/questions/3786881/what-is-a-method-in-python), the answer by AndiDog, not the most voted one. In short, a method is a function defined in a class definition. 

* __What is the use of `-m` in the command `python -m themodule`?__

	Two uses. One is in the case that you're in some directory other than the path in `sys.path`, but you want to run a built-in module, like `SimpleHTTPServer`. Another is when your objective module is in the path `dira/`, but it requires external modules in `dirb/`, then you can walk into `dirb/` and run `python -m dira/yourmodule`. The underlying reason is that `-m` will search along `sys.path`, and current working diretory will be the first path in `sys.path`. By the way, `__name__` is always `__main__` with or without `-m`. 
