

CSV About
=========
* CSV - Comma/Character Separated Values
* No CSV formal standard, just a good practice
* Flat file (2D) without relations
* Relations has to be flatten (serialization, additional columns, etc...)
* Typically first line (header) represents column names
* Rarely first line can also have a structure (nrows, ncols)
* Internationalization: encoding
* Localization: decimal separator, thousands separator, date format
* Parameters: delimiter, quotechar, quoting, lineterminator, dialect


Header
------


Delimiter
---------
* ``csv`` module expects delimeter to be 1-character in length


Quotechar
---------
* ``"`` - quote char (best)
* ``'`` - apostrophe


Quoting
-------
* ``csv.QUOTE_ALL`` (safest)
* ``csv.QUOTE_MINIMAL``
* ``csv.QUOTE_NONE``
* ``csv.QUOTE_NONNUMERIC``


Lineterminator
--------------
* ``\r\n`` - New line on Windows
* ``\n`` - New line on ``*nix``
* ``*nix`` operating systems: Linux, macOS, BSD and other POSIX compliant OSes (excluding Windows)


Decimal Separator
-----------------
* ``0.1`` - Decimal point
* ``0,1`` - Decimal comma


Thousands Separator
-------------------
* ``1000000`` - None
* ``1'000'000`` - Apostrophe
* ``1 000 000`` - Space, the internationally recommended thousands separator
* ``1.000.000`` - Period, used in many non-English speaking countries
* ``1,000,000`` - Comma, used in most English-speaking countries


Date and Time
-------------


Encoding
--------
* ``utf-8`` - international standard (should be always used!)
* ``iso-8859-1`` - ISO standard for Western Europe and USA
* ``iso-8859-2`` - ISO standard for Central Europe (including Poland)
* ``cp1250`` or ``windows-1250`` - Central European encoding on Windows
* ``cp1251`` or ``windows-1251`` - Eastern European encoding on Windows
* ``cp1252`` or ``windows-1252`` - Western European encoding on Windows
* ``ASCII`` - ASCII characters only


Dialects
--------


Good Practices
--------------


CSV Format Read
===============


CSV Format Write
================


CSV Non-Standard
================


Ini
---
* setup.cfg
* ``delimiter='='``


Config
------
* ``/etc/postgresql/*/main/postgresql.conf``
* ``delimiter=' = '``


Toml
----
* pyproject.toml
* ``delimiter='='``


Passwd
------
* ``/etc/passwd``
* ``delimiter=':'``


SSHd Config
-----------
* ``/etc/ssh/sshd_config``
* ``delimiter=' '``


Hosts
-----
* ``delimiter='\s+'``


Crontab
-------
* ``/etc/crontab``
* ``delimiter='\s+'``


Key-Value
---------
* ``/etc/locate.rc``
* ``delimiter='='``


Docker
------
* ``.env`` from Docker
* ``delimiter='='``


Sensors
-------
* ``delimiter=';'``


CSV Reader
==========
* Reads CSV file to list[list]
* ``csv.reader()``
* Default encoding is ``encoding='utf-8'``


Minimal
-------
* Default mode is ``mode='r'``


Parametrized
------------


CSV Writer
==========
* Writes iterable of iterables (eg. list[list], list[tuple]) to CSV file
* ``csv.writer()``
* Remember to add ``mode='w'`` to ``open()`` function
* Default encoding is ``encoding='utf-8'``


Minimal
-------


Parametrized
------------


CSV DictReader
==============
* * Reads CSV file to list[dict]
* ``csv.DictReader()``


Minimal
-------


Parametrized
------------


Custom Header
-------------


CSV DictWriter
==============
* Writes iterable of dicts (eg. list[dict]) to CSV file
* ``csv.DictWriter()``
* Remember to add ``mode='w'`` to ``open()`` function
* Default encoding is ``encoding='utf-8'``


Minimal
----------


Parametrized
------------
