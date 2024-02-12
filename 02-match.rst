

Match About
===========
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial
* Significantly faster for sequences and mappings [#Shaw2022]_
* Since Python 3.11: For sequences if faster around 80% [#Shaw2022]_
* Since Python 3.11: For mappings if faster around 80% [#Shaw2022]_
* https://github.com/python/cpython/blob/main/Grammar/python.gram#L479


Problem
-------


Pattern Matching
----------------


Syntax
------


Patterns
--------
* literal pattern
* capture pattern
* wildcard pattern
* constant value pattern
* sequence pattern
* mapping pattern
* class pattern
* OR pattern
* walrus pattern


Recap
-----
* ``x`` - assign ``x = subject``
* ``'x'`` - test ``subject == 'x'``
* ``x.y`` - test ``subject == x.y``
* ``x()`` - test ``isinstance(subject, x)``
* ``{'x': 'y'}`` - test ``isinstance(subject, Mapping) and subject.get('x') == 'y'``
* ``['x']`` - test ``isinstance(subject, Sequence) and len(subject) == 1 and subject[0] == 'x'``
* Source: [#Hettinger2021]_


Further Reading
---------------
* https://peps.python.org/pep-0622/
* https://peps.python.org/pep-0636/


Match Literal
=============
* https://peps.python.org/pep-0622/#literal-patterns


With Strings
------------


With Numbers
------------


With Booleans
-------------


Match Or
========


Use Code - 0x01
---------------


Match Capture
=============
* https://peps.python.org/pep-0622/#capture-patterns


Match Wildcard
==============
* https://peps.python.org/pep-0622/#wildcard-pattern


Match Constant
==============
* https://peps.python.org/pep-0622/#constant-value-patterns


Match Sequence
==============
* https://peps.python.org/pep-0622/#sequence-patterns


Match Mapping
=============
* https://peps.python.org/pep-0622/#mapping-patterns


Args, Kwargs
------------


Match Class
===========
* https://peps.python.org/pep-0622/#class-patterns


Match Guard
===========
* Additional if statements
* This is not to replace if-else expression
* This add additional validation to match-case
* https://peps.python.org/pep-0622/#guards


Match Sub-patterns
==================


Match Walrus
============


Assignment Expression
---------------------
* A.K.A. Walrus Operator
* ``re.match()`` returns ``re.Match | None``
