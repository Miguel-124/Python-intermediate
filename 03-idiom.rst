

Idiom About
===========
* Returns iterator
* Generator-like - behaves similarly, but is not a generator
* ``range(start, stop, step)``
* ``reversed(iterable)``
* ``enumerate(iterable, start=0)``
* ``zip(*iterable, strict=False)``
* ``map(func, iterable)``
* ``filter(func, iterable)``
* ``next(iterable)``
* ``iter(iterable)``
* ``chain(*iterator)``
* any, all, min, max, sum
* zip, enumerate, chain
* map, filter, reduce, starmap, zip_longest
* range, product, permutations
* partial


Comprehension
-------------
* all value > 1.0


Map
---


Idiom Range
===========
* Return sequence of numbers
* It is not a generator
* Generator (lazy evaluated)
* ``range([start], <stop>, [step])``
* optional ``start``, inclusive, default: ``0``
* required ``stop``, exclusive,
* optional ``step``, default: ``1``


Problem
-------


Solution
--------


Lazy Evaluation
---------------


Itertools
---------
* Learn more at https://docs.python.org/3/library/itertools.html
* More information in `Itertools`
* ``itertools.count(start=0, step=1)``


Idiom Reversed
==============
* ``reversed(sequence, /)``
* Return a reverse iterator over the values of the given sequence


Idiom Enumerate
===============
* Enumerate sequences
* Built-in generator like (lazy evaluated)
* ``enumerate(*iterables)``
* required ``*iterables`` - 1 or many sequences or iterator object
* Return an enumerate object
* The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.


Problem
-------


Solution
--------


Lazy Evaluation
---------------


Dict Conversion
---------------


Using in a Loop
---------------


Idiom Zip
=========
* Combine two sequences
* Generator (lazy evaluated)
* ``zip(*iterables, strict=False)``
* required ``*iterables`` - 1 or many sequences or iterator object
* Iterate over several iterables in parallel, producing tuples with an item from each one.


Problem
-------


Solution
--------


Lazy Evaluation
---------------


Generate Dict
-------------


Adjusts to the Shortest
-----------------------
* ``zip()`` adjusts to the shortest


Adjust to the Longest
---------------------
* ``itertools.zip_longest(iter1 [,iter2 [...]], [fillvalue=None]) --> zip_longest object``


Three-way merge
---------------


In For Loop
-----------


Unzip
-----


Strict
------
* ``zip(*iterables, strict=False)``
* Since Python 3.10: :pep:`618` -- Add Optional Length-Checking To zip [#pep618]_
* Source [#pydoczip]_


Zip Longest
-----------


Idiom All
=========
* Return True if all elements of the iterable are true (or if the iterable is empty).
* Built-in (evaluated)


Solution
--------


Performance
-----------


Idiom Any
=========
* Return True if any element of the iterable is true.
* If the iterable is empty, return False.
* Built-in (evaluated)


Solution
--------


Idiom Map
=========
* Map (convert) elements in sequence
* Generator (lazy evaluated)
* ``map(callable, *iterables)``
* required ``callable`` - Function
* required ``iterables`` - 1 or many sequence or iterator objects


Problem
-------


Solution
--------


Lazy Evaluation
---------------


Multi Parameters
----------------


Starmap
-------


Partial
-------


More Args
---------


Performance
-----------


Idiom Filter
============
* ``filter(callable, *iterables)``
* Select elements from sequence
* Generator (lazy evaluated)
* required ``callable`` - Function
* required ``iterables`` - 1 or many sequence or iterator objects


Not-a-Generator
---------------


Problem
-------


Solution
--------


Lazy Evaluation
---------------


Performance
-----------


Idiom Apply
===========


Idiom Reduce
============
* Reduce sequence using function
* Built-in


Syntax
------
* ``functools.reduce(function, iterable[, initializer])``
* required ``callable`` - Function
* required ``iterable`` - Sequence or iterator object
* https://docs.python.org/library/functools.html


Problem
-------


Solution
--------


Rationale
---------
* https://docs.python.org/library/operator.html


Map Reduce
----------
* https://dask.org


Idiom Next
==========


Range
-----


Enumerate
---------


Zip
---


Map
---


Filter
------


Idiom Iter
==========


Range
-----


Enumerate
---------


Zip
---


Idiom Chain
===========
* ``itertools.chain()``
* Generator like (lazy evaluated)


Idiom Patterns
==============
* Python ``for`` loop is equivalent to ``forEach`` in other languages
* Other languages ``for`` loop is Python's ``while`` (sic!)


Loop Patterns
-------------


Range
-----


ForEach
-------


Sum
---


Enumerate
---------


Zip
---


List Comprehension
------------------


Set Comprehension
-----------------


Dict Comprehension
------------------


Map
---


Filter
------


For Else
--------


While Else
----------


Str Startswith
--------------


Str Endswith
------------


Str Join Newline
----------------


Others
------
* ``all()``
* ``any()``
* ``iter()``
* ``next()``


Functools
---------
* https://docs.python.org/3/library/functools.html
* ``from functools import *``
* ``functools.reduce(function, iterable[, initializer])``


Itertools
---------
* https://docs.python.org/3/library/itertools.html
* More information in `Itertools`
* ``itertools.from itertools import *``
* ``itertools.count(start=0, step=1)``
* ``itertools.cycle(iterable)``
* ``itertools.repeat(object[, times])``
* ``itertools.accumulate(iterable[, func, *, initial=None])``
* ``itertools.chain(*iterables)``
* ``itertools.compress(data, selectors)``
* ``itertools.islice(iterable, start, stop[, step])``
* ``itertools.starmap(function, iterable)``
* ``itertools.product(*iterables, repeat=1)``
* ``itertools.permutations(iterable, r=None)``
* ``itertools.combinations(iterable, r)``
* ``itertools.combinations_with_replacement(iterable, r)``
* ``itertools.groupby(iterable, key=None)``


Idiom Itertools
===============
* Learn more at https://docs.python.org/3/library/itertools.html
* More information in `Itertools`
* ``itertools.count(start=0, step=1)``
* ``itertools.cycle(iterable)``
* ``itertools.repeat(object[, times])``
* ``itertools.accumulate(iterable[, func, *, initial=None])``
* ``itertools.chain(*iterables)``
* ``itertools.compress(data, selectors)``
* ``itertools.islice(iterable, start, stop[, step])``
* ``itertools.starmap(function, iterable)``
* ``itertools.product(*iterables, repeat=1)``
* ``itertools.permutations(iterable, r=None)``
* ``itertools.combinations(iterable, r)``
* ``itertools.combinations_with_replacement(iterable, r)``
* ``itertools.groupby(iterable, key=None)``
