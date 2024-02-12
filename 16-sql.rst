

SQL About
=========


SQL Data Types
==============
* Python ``None``  -> SQLite3 ``NULL``
* Python ``int``   -> SQLite3 ``INTEGER``
* Python ``float`` -> SQLite3 ``REAL``
* Python ``str``   -> SQLite3 ``TEXT``
* Python ``bytes`` -> SQLite3 ``BLOB``


NULL Type
---------
* The value is a undefined value


INTEGER Type
------------
* The value is a signed integer
* Stored in 1, 2, 3, 4, 6, or 8 bytes
* Depending on the magnitude of the value


REAL Type
---------
* The value is a floating point value
* Stored as an 8-byte IEEE floating point number


TEXT Type
---------
* The value is a text string
* Stored using the database encoding (ie. UTF-8)


BLOB Type
---------
* Binary Large Object
* The value is a blob of data
* Stored exactly as it was input


NUMERIC Affinity
----------------
* May contain values using all five storage classes


DATETIME Affinity
-----------------


SQL Constraints
===============
* Does something automatically
* Prevents from duplicating information
* Prevents from loss of integrity


NOT NULL
--------
* Ensures that a column cannot have a ``NULL`` value


UNIQUE
------
* Ensures that all values in a column are different


PRIMARY KEY
-----------
* Uniquely identifies each row in a table
* A combination of a ``NOT NULL`` and ``UNIQUE``


FOREIGN KEY
-----------
* Uniquely identifies a row/record in another table


CHECK
-----
* Ensures that all values in a column satisfies a specific condition


DEFAULT
-------
* Sets a default value for a column when no value is specified


INDEX
-----
* Used to create and retrieve data from the database very quickly
* Analog to notebook calendar tabs


SQL Table
=========
* Constraint ``UNIQUE``
* Constraint ``PRIMARY KEY``
* Constraint ``DEFAULT``
* Constraint ``NOT NULL``
* Auto-value ``NULL``
* Auto-value ``AUTOINCREMENT``
* Auto-value ``CURRENT_TIME``
* Auto-value ``CURRENT_DATE``
* Auto-value ``CURRENT_TIMESTAMP``
* Function ``STRFTIME()``, ``DATETIME()``


Create Table
------------


Add Column
----------


Drop Column
-----------
* SQLite3 does not support dropping columns with ``ALTER TABLE``
* We have to do a workaround instead


SQL Index
=========
* Used to create and retrieve data from the database very quickly
* Analog to notebook calendar tabs


Index Types
-----------
* Column Index
* Multi Column Index
* Partial Index
* Functional Index
* Binary Index


SQL Syntax
----------


If Not Exists
-------------
* ``IF NOT EXISTS``


Unique Index
------------
* ``UNIQUE``


SQL Insert
==========


Insert Values
-------------


Insert Values to Columns
------------------------


Insert to Autoincrement Column
------------------------------


Prepared statements
-------------------


SQL Update
==========


Update One
----------


Update Many Columns
-------------------


Update Many Rows
----------------


SQL Delete
==========
* Write your statement starting with ``--`` after you're done, make sure


Delete One
----------
* Removes data from table
* Leaves table structure intact
* Can be narrowed down by a ``WHERE``


Delete Many
-----------
* Removes data from table
* Leaves table structure intact
* Can be narrowed down by a ``WHERE``


Delete Query
------------
* Removes data from table
* Leaves table structure intact
* Can be narrowed down by a ``WHERE``


Truncate
--------
* Removes all the data
* Leaves table structure intact


Drop
----
* Removes all the data
* Removes table too


SQL Transaction
===============
* Any command that accesses the database will automatically start a transaction
* Automatically started transactions are committed when the last SQL statement finishes
* Transactions can be started manually using the BEGIN command.
* Transactions usually persist until the next COMMIT or ROLLBACK command.
* ACID - four standard properties
* Atomicity
* Consistency
* Isolation
* Durability


ACID
----


Begin
-----
* Starts a transaction
* ``BEGIN`` or ``BEGIN TRANSACTION``


Rollback
--------
* Perform a revert of all operations


Commit
------
* Executes all operations
* ``COMMIT`` or ``END TRANSACTION``


SQL Select From
===============


All Columns
-----------


Selected Columns
----------------


Column Name Aliases
-------------------


SQL Select Limit
================


Limit Results
-------------


Pagination
----------


SQL Select Order By
===================


Order By
--------


Ascending
---------
* From smallest to biggest
* ``ASC``


Descending
----------
* From biggest to smallest
* ``DESC``


Multiple
--------
* When first criteria is the same


Empty
-----
* ``NULLS FIRST``
* ``NULLS LAST``


SQL Select Where
================
* Order clauses to filter out the most data first!


Selection
---------
* ``=`` - equals
* ``!=`` - not equal
* ``<>`` - not equal
* ``>`` - greater then
* ``>=`` - greater or equal
* ``<`` - less than
* ``<=`` - less or equal


Conjunction
-----------
* ``AND`` - conjunction


Alternative
-----------
* ``OR`` - alternative


Contains
--------
* ``IN`` - contains
* ``NOT IN`` - not contains


Identity
--------
* ``IS`` - identity check
* ``IS NOT`` - negation of an identity check


Like
----
* ``LIKE``
* ``%`` - Any character (many)
* ``_`` - Any character (one)


SQL Select Group By
===================


Group By
--------


Having
------


SQL Select Subquery
===================
* ``IN (SELECT ...)`` - subquery


Subqueries
----------


SQL Select Distinct
===================
* Unique values


Distinct
--------


Alias
-----


With Query
----------


SQL Select Functions
====================


Sum
---


Average
-------


Count
-----


SQL Join
========
* Combine records from two or more tables in a database
* Combining fields from two tables by using values common to each


INNER JOIN
----------
* Returns rows when there is a match in both tables
* The most important and frequently used of the joins


LEFT JOIN
---------
* Returns all rows from the left table, even if there are no matches


RIGHT JOIN
----------
* Returns all rows from the right table, even if there are no matches


FULL JOIN
---------
* Combines the results of both left and right outer joins
* The joined table will contain all records from both the tables and fill


OUTER JOIN
----------


SELF JOIN
---------
* Is used to join a table to itself as if the table were two tables
* Temporarily renaming at least one table in the SQL statement


CARTESIAN JOIN
--------------
* Also known as ``CROSS JOIN``
* Returns the Cartesian product of the sets of records from the two


SQL Injection
=============


Scenario
--------


SQL Views
=========


SQL Explain
===========


SQL Use Cases
=============
