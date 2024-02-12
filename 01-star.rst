

Star Assignment
===============
* ``a, b, *c = 1, 2, 3, 4, 5``
* Used when there is arbitrary number of values to unpack
* Could be used from start, middle, end
* There can't be multiple star expressions in one assignment statement
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future


Arbitrary Number of Arguments
-----------------------------


Errors
------


Skipping Values
---------------
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future


For Loop Unpacking
------------------


Multi Dimensional
-----------------


Merge
-----


Star Signature
==============
* Define API for you functions
* Require particular way of passing positional and optional parameters
* All parameters after ``*`` must be keyword-only
* All parameters before ``/`` must be positional-only
* ``*`` could be anywhere, not only at the beginning
* ``/`` could be anywhere, not only at the end
* Since Python 3.8: :pep:`570` -- Python Positional-Only Parameters


Recap
-----
* Positional arguments - value passed to function
* Positional arguments - order is important
* Positional arguments - must be at the left side
* Keyword arguments - value passed to function resolved by name
* Keyword arguments - order is not important
* Keyword arguments - must be on the right side
* Positional argument cannot follow keyword arguments


Keyword-only Parameters
-----------------------
* All parameters after ``*`` must be keyword-only
* ``*`` could be anywhere, not only at the beginning


Positional-only Parameters
--------------------------
* Since Python 3.8: :pep:`570` -- Python Positional-Only Parameters
* All parameters before ``/`` must be positional-only
* ``/`` could be anywhere, not only at the end


Positional and Keyword Parameters
---------------------------------


Star Parameters
===============
* ``*`` is used for positional parameters
* ``args`` is a convention, but you can use any name
* ``*args`` unpacks to ``tuple``
* ``**`` is used for keyword parameters
* ``kwargs`` is a convention, but you can use any name
* ``**kwargs`` unpacks to ``dict``


Syntax
------


Recap
-----
* Parameter - Receiving variable used within the function
* Required parameters - Parameter which is necessary to call function
* Optional parameters - Parameter which is optional and has default value (if not specified at call time)
* Optional parameter - also known as: parameter with default value


Positional Parameters
---------------------
* ``*`` is used for positional parameters
* ``args`` is a convention, but you can use any name
* ``*args`` unpacks to ``tuple``


Keyword Parameters
------------------
* ``**`` is used for keyword parameters
* ``kwargs`` is a convention, but you can use any name
* ``**kwargs`` unpacks to ``dict``


Positional and Keyword Parameters
---------------------------------
* ``*`` is used for positional parameters
* ``**`` is used for keyword parameters
* ``*args`` unpacks to ``tuple``
* ``**kwargs`` unpacks to ``dict``


Parameters with Args, Kwargs
----------------------------


Merge
-----


Star Arguments
==============
* Unpack and Arbitrary Number of Parameters and Arguments


Recap
-----
* Argument - Value or variable being passed to the function
* Positional arguments - value passed to function
* Positional arguments - order is important
* Positional arguments - must be at the left side
* Keyword arguments - value passed to function resolved by name
* Keyword arguments - order is not important
* Keyword arguments - must be on the right side
* Positional argument cannot follow keyword arguments


Positional Arguments
--------------------
* ``*`` is used for positional arguments
* there is no convention, but you can use any name
* ``*`` unpacks from ``tuple``, ``list`` or ``set``


Keyword Arguments
-----------------
* ``**`` is used for keyword arguments
* there is no convention, but you can use any name
* ``**`` unpacks from ``dict``


Positional and Keyword Arguments
--------------------------------


Create One Object
-----------------


Create Many Objects
-------------------


Recap
-----
