

SQLite3 About
=============
* The most popular database in the world
* File database with
* Open Source (Public Domain license), written in C
* It is only 699 KiB
* Supports for SQL-92 standard (Postgres flavor)
* SQLite3 is built in in Python
* It is used by mobile apps on iOS, Android, etc.
* Almost every app has it's own sqlite3 database
* Almost every web browser (on desktop) uses SQLite3 database
* https://sqlitebrowser.org/


Limits
------
* Maximum database size: 281 terabytes
* Maximum number of rows in a table: 2**64 (1.8e+19)
* Maximum number of columns in a table: 2000
* Maximum Number Of Tables In A Schema: 2147483646 (a little over 2 billion)
* Maximum BLOB size: 2147483647 (2**31 - 1)
* Maximum bytes of SQL statement: 1,000,000,000
* Maximum tables in a join: 64 tables
* Maximum number of arguments on a function: 127
* Maximum number of terms in a compound select statement: 500
* Maximum length of a LIKE or GLOB pattern: 50000
* Only partially provides triggers
* Cannot write to views
* https://sqlite.org/limits.html


Installation
------------


Verification
------------


DB API v2
---------


Command-line interface
----------------------
* New in version 3.12


SQLite3 Connect
===============
* File database - persistent storage
* In-memory - very fast, but volatile
* sqlite3.connect() -> connection
* connection.close()


In-Memory Database
------------------
* Useful for tests, development and demonstrations
* Very fast (do not write any data to disk)
* Remember to close connection


File Database
-------------
* Connection will create file if not exists
* Remember to close connection


Context Managers
----------------
* Prefer using context manager
* No need to remember about closing connection
* Prepare your data and statements before connection
* Works with either in-memory or file database


Debug
-----
* ``conn.set_trace_callback(print)``
* Registers trace_callback to be called for each SQL statement that is actually executed by the SQLite backend.
* The only argument passed to the callback is the statement (as string) that is being executed.


SQLite3 Adapter/Converter
=========================
* https://docs.python.org/3.12/library/sqlite3.html#sqlite3-adapter-converter-recipes


Adapter
-------


Converter
---------


SQLite3 Execute
===============


Create Table
------------


Create Index
------------


SQLite3 Insert Sequence
=======================


Insert One
----------


Insert Many
-----------


SQLite3 Insert Mapping
======================


Insert One
----------


Insert Many
-----------


SQLite3 Insert Constraints
==========================


Unique
------


Programming Error
-----------------


Operational Error
-----------------


SQLite3 Fetch
=============
* Fetch as `list[tuple]` / `list[list]`
* Fetch as `list[Row]` / `list[dict]`
* `sqlite3.row_factory`


Fetch Sequences
---------------


Fetch Mappings
--------------


SQLite3 Cursor
==============
* ``db.cursor() -> cursor``
* ``cursor.lastrowid``


Create Cursor
-------------


Last Row ID
-----------


SQLite3 Join
============


SQLite3 Use Cases
=================


Pandas
------


Sensors
-------
