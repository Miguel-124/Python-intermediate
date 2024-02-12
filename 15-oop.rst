

OOP Mutability
==============
* Function and method arguments should not be mutable


Problem
-------


Rationale
---------


Solution
--------


OOP Access Modifiers
====================
* Attributes and methods are always public
* No protected and private keywords
* Private and protected is only by convention [#pydocprivatevar]_
* ``name`` - public attribute
* ``_name`` - protected attribute (non-public by convention)
* ``__name`` - private attribute (name mangling)
* ``__name__`` - system attribute (dunder)
* ``name_`` - avoid name collision with built-ins


Public Attribute
----------------
* ``name`` - public attribute


Protected Attribute
-------------------
* ``_attrname`` - protected attribute (non-public by convention)


Private Attribute
-----------------
* ``__attrname`` - private attribute (name mangling)


Name Mangling
-------------


Name Collision
--------------
* Example colliding names: ``type_``, ``id_``, ``hash_``


System Attributes
-----------------
* ``__attrname__`` - Current module
* ``obj.__class__`` - Class from which object was instantiated
* ``obj.__dict__`` - Stores instance variables
* ``obj.__doc__`` - Object docstring
* ``obj.__annotations__`` - Object attributes type annotations
* ``obj.__module__`` - Name of a module in which object was defined


Show Attributes
---------------
* ``vars()`` display ``obj.__dict__``


OOP ClassVar
============
* Class Variables
* Instance Variables
* Type Annotations


Class Variables
---------------
* Fields defined on a class
* Must have default values
* Share state
* Also known as 'static attributes'


Instance Variables
------------------
* Fields defined on an instance
* Do not share state (unless mutable argument in method signature)
* By convention initialized in ``__init__()``
* Also known as 'dynamic attributes'


Class and Instance Variables
----------------------------


Annotations
-----------


Dataclass Fields
----------------
* Dataclass uses class variables notation to create instance fields
* Dataclass do not validate type annotations, unless ``ClassVar``


Init Variables
--------------


Class vs. Instance Variables
----------------------------


Mechanism
---------
* ``vars(obj)`` is will return ``obj.__dict__``


OOP Property
============
* Disable attribute modification
* Logging value access


OOP Object Relations
====================
* ORM - Object-relational mapping
* Converts (`map`) between objects in code and database tables (`relations`)
* Declarative - First define model, which then maps to the database tables
* ``pickle`` - has relations
* ``json`` - has relations
* ``csv`` - non-relational format


Pros
----


Cons
----
