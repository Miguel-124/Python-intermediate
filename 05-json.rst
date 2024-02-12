

JSON About
==========
* JavaScript Object Notation
* The most popular format for data exchange


JSON or Python?
---------------
* JSON format is similar to ``dict`` notation in Python
* Fields are always enclosed only by double quote ``"`` character
* Instead of ``True`` there is ``true`` (lowercase)
* Instead of ``False`` there is ``false`` (lowercase)
* Instead of ``None`` there is ``null``
* ``list`` is known as ``array`` (despite the same syntax)
* ``dict`` is known as ``object`` (despite the same syntax)
* There is no ``tuple`` or ``set``
* Coma ``,`` is not allowed after the last element in list or object
* ``camelCase`` is convention, although ``snake_case`` is also valid
* Unicode characters are stored as unicode entities (``"cze\\u015b\\u0107"``)


Pretty Printing JSON
--------------------
* JSON can be minified to save space for network transmission
* It is not very readable


JSON String
===========


Mapping
-------
* ``json.dumps(DATA: dict) -> str`` - dict to JSON
* ``json.loads(DATA: str) -> dict`` - JSON to dict


List of Mappings to JSON
------------------------
* ``json.dumps(data: Iterable[dict]) -> str`` - list[dict] to JSON
* ``json.loads(data: str) -> list[dict]`` - JSON to list[dict]


List of Iterable
----------------
* ``json.dumps(data: list[Iterable]) -> str`` - list[Iterable] to JSON
* ``json.loads(data: str) -> list[list]`` - JSON to list[Iterable]


JSON File
=========
* ``json.load(file) -> dict``
* ``json.dump(data, file) -> None``
* file extension ``.json``


Write Data to JSON File
-----------------------
* ``json.dump(data, file) -> None``
* file extension ``.json``


Read Data From JSON File
------------------------
* ``json.load(file) -> dict``
* file extension ``.json``


JSON Encoder
============
* Problem with ``date``, ``datetime``, ``time``, ``timedelta``
* Exception during encoding datetime
* Encoder will be used, when standard procedure fails


Problem
-------


Default Function with Lambda
----------------------------


Default Function with If
------------------------


Default Function with Match
---------------------------


Monkey Patching with Lambda Expression
--------------------------------------


Dependency Injection
--------------------


JSON Decoder
============


Problem
-------
* Problem with ``date``, ``datetime``, ``time``, ``timedelta``
* Python does not decode values automatically


Problem
-------


Function Decoder
----------------
* This works for simple (flat) data
* This works for nested data structures


Context Dependency Injection
----------------------------


JSON Object
===========


Encode Object
-------------


Decode Object
-------------


Object Encoder
--------------


Object Decoder
--------------


Encode Object with Relation
---------------------------


Decode
------
