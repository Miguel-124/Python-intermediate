

File Path Relative
==================
* Python works with both relative and absolute path
* Path is relative to currently running script
* Path separator ``\`` (backslash) is used on Windows
* Path separator ``/`` (slash) is used on ``*nix`` operating systems: Linux,


Current Directory
-----------------
* Path is relative to currently running script
* ``.`` - Current directory


Upper Directory
---------------
* Path is relative to currently running script
* ``..`` - Parent directory


Current Working Directory
-------------------------
* Returns an absolute path to current working directory


Good Practices
--------------
* Never hardcode paths, use constant as a file name or file path
* Convention (singular form): ``FILE``, ``FILENAME``, ``FILEPATH``, ``PATH``
* Convention (plural form): ``FILES``, ``FILENAMES``, ``FILEPATHS``, ``PATHS``
* Note, that ``PATH`` is usually used for other purposes (``sys.path`` or


File Path Absolute
==================
* Python works with both relative and absolute path
* Path separator ``\`` (backslash) is used on Windows
* Path separator ``/`` (slash) is used on ``*nix`` operating systems: Linux,


Absolute Path
-------------
* Absolute path on Windows starts with drive letter
* Absolute path on ``*nix`` starts with root ``/`` dir
* Absolute path include all entries in the directories hierarchy


Escaping Characters in Path
---------------------------
* "\\ " (backslash space) - escapes space
* Note that in Python escapes in paths are not required


Convert Relative Path to Absolute
---------------------------------


Dirname, Filename
-----------------


Script Path
-----------
* ``__file__`` - Returns an absolute path to currently running script


File Path Problem
=================


Recap
-----
* Raw Strings
* Always use raw-strings (``r"..."``) for paths
* Raw String turns-off escape characters
* "\\ " (backslash space) - escapes space
* Note that in Python escapes in paths are not required


Setup
-----


Escaping Characters in Path
---------------------------
* "\\ " (backslash space) - escapes space
* Note that in Python escapes in paths are not required


File Path Modify
================


Create Directories
------------------


Create Directory Hierarchy
--------------------------


Delete directory
----------------


Create File
-----------
* Touch creates a file


Check If Exists
---------------


Is File or Dir
--------------


File Encoding
=============
* ``utf-8`` - a.k.a. Unicode - international standard (should be always used!)
* ``iso-8859-1`` - ISO standard for Western Europe and USA
* ``iso-8859-2`` - ISO standard for Central Europe (including Poland)
* ``cp1250`` or ``windows-1250`` - Central European encoding on Windows
* ``cp1251`` or ``windows-1251`` - Eastern European encoding on Windows
* ``cp1252`` or ``windows-1252`` - Western European encoding on Windows
* ``ASCII`` - ASCII characters only
* Since Windows 10 version 1903, UTF-8 is default encoding for Notepad!


Str vs Bytes
------------
* That was a big change in Python 3
* In Python 2, str was bytes
* In Python 3, str is unicode (UTF-8)


UTF-8
-----


Unicode Encode Error
--------------------


Unicode Decode Error
--------------------


Escape Characters
-----------------
* ``\r\n`` - is used on windows
* ``\n`` - is used everywhere else
* More information in `Builtin Printing`
* Learn more at https://en.wikipedia.org/wiki/List_of_Unicode_characters


Files Binary
============
* Text I/O over a binary storage (such as a file) is significantly slower


Append Binary
-------------
* ``mode='ab'`` - append in binary mode


Write Binary
------------
* ``mode='wb'`` - write in binary mode


Read Binary
-----------
* ``mode='rb'`` - read in binary mode


Pickle
------
* Works with any Python object (variables, functions, classes, nested objects)
* More information in `Serialization Pickle`


Seek
----
* Go to the n-th byte in the file
* Supports negative index (from end of file)
