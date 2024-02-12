

Generator About
===============
* Processes one element at a time
* Does not remember previous element
* Does not know next element
* Can be used only once
* Save memory (does not require more memory for processing large data)
* Uses around 10% more CPU than regular processing
* Typical usage: streams, processing larger than memory files or data
* Cannot use ``len()`` as of generators don't have length
* Previous element is overridden by current on ``next()``
* Functions (list, dict, tuple, frozenset, set, sum, all, any, etc)


Inspect
-------


Generator Expression
====================
* Comprehensions executes instantly
* Comprehensions are stored in the memory until end of a program
* Comprehensions should be used when accessing values more than one
* Generator Expressions are lazy evaluated
* Generator Expressions are cleared once they are executed
* Generator Expressions should be used when accessing value once (for example in the loop)


List Comprehension
------------------
* Comprehensions executes instantly
* Comprehensions will be in the memory until end of a program
* Comprehensions - Using values more than one


Generator Expression
--------------------
* Generators are lazy evaluated
* Creates generator object and assign reference
* Code is not executed instantly
* Sometimes code is not executed at all!
* Are cleared once they are executed
* Generator will calculate next number for every loop iteration
* Generator forgets previous number
* Generator doesn't know the next number
* It is used for one-time access to values


Comprehensions or Generator Expression
--------------------------------------
* If you need values evaluated instantly, there is no point in using generators


Why Round Brackets?
-------------------
* Round brackets does not produce tuples (commas does)
* Round brackets bounds context


Generator Function
==================
* ``yield`` keyword turns function into generator function


Recap
-----


Definition
----------


Call Generator
--------------


Get Results
-----------
* All generators implements Iterator protocol
* Iterator has ``obj.__iter__()`` method which enable use of ``iter(obj)``
* Iterator has ``obj.__next__()`` method which enable use of ``next(obj)``


Yield Keyword
-------------


Yield in a Loop
---------------


Yields in Loops
---------------


Yield in a Zip Loop
-------------------


Generator Inspect
=================


Is Generator
------------


Introspection
-------------


Memory Footprint
----------------
* ``sys.getsizeof(obj)`` returns the size of an ``obj`` in bytes
* ``sys.getsizeof(obj)`` calls ``obj.__sizeof__()`` method
* ``sys.getsizeof(obj)`` adds an additional garbage collector overhead if the ``obj`` is managed by the garbage collector


Generator Yield From
====================
* Since Python 3.3: :pep:`380` -- Syntax for Delegating to a Subgenerator
* Helps with refactoring generators
* Useful for large generators which can be split into smaller ones
* Delegation call
* ``yield from`` terminates on ``GeneratorExit`` from other function
* The value of the ``yield from`` expression is the first argument to the ``StopIteration`` exception raised by the iterator when it terminates
* Return expr in a generator causes ``StopIteration(expr)`` to be raised upon exit from the generator


Why?
----


Execute
-------


Itertools Chain
---------------


Delegation call
---------------


Yield From Sequences
--------------------


Yield From Comprehensions
-------------------------


Yield From Generator Expression
-------------------------------


Conclusion
----------
* Python yield keyword creates a generator function.
* It's useful when the function returns a large amount of data by


Generator Send
==============
* ``.send()`` method allows to pass value to the generator
* ``data = yield`` will receive this "sent" value


Why Send None?!
---------------
* After running you have to send ``None`` value to begin processing
* Sending anything other will raise ``TypeError``


Send Upstream Cascade
---------------------


Generator Itertools
===================


Itertools
---------
* Learn more at https://docs.python.org/library/itertools.html
* More information in `Itertools`
* ``from itertools import *``
* ``count(start=0, step=1)``
* ``cycle(iterable)``
* ``repeat(object[, times])``
* ``accumulate(iterable[, func, *, initial=None])``
* ``chain(*iterables)``
* ``compress(data, selectors)``
* ``islice(iterable, start, stop[, step])``
* ``starmap(function, iterable)``
* ``product(*iterables, repeat=1)``
* ``permutations(iterable, r=None)``
* ``combinations(iterable, r)``
* ``combinations_with_replacement(iterable, r)``
* ``groupby(iterable, key=None)``


Itertools Count
---------------
* ``itertools.count(start=0, step=1)``


Itertools Cycle
---------------
* ``itertools.cycle(iterable)``


Itertools Repeat
----------------
* ``itertools.repeat(object[, times])``


Itertools Accumulate
--------------------
* ``itertools.accumulate(iterable[, func, *, initial=None])``


Itertools Chain
---------------


Itertools Compress
------------------


Itertools ISlice
----------------
* ``itertools.islice(iterable, start, stop[, step])``


Itertools Starmap
-----------------
* ``itertools.starmap(function, iterable)``


Itertools Product
-----------------
* ``itertools.product(*iterables, repeat=1)``


Itertools Permutations
----------------------
* ``itertools.permutations(iterable, r=None)``


Itertools Combinations
----------------------
* ``itertools.combinations(iterable, r)``


Itertools Combinations With Replacement
---------------------------------------
* ``itertools.combinations_with_replacement(iterable, r)``


Itertools GroupBy
-----------------
* ``itertools.groupby(iterable, key=None)``
* Make an iterator that returns consecutive keys and groups from the
