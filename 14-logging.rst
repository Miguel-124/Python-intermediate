

Logging About
=============
* Do not print
* Always use logger
* Logs can be displayed on console
* Logs can be redirected to file
* Logs can be redirected to database
* Logs can be silenced (certain level)
* Logs can be rotated
* Logs can change format


Further Reading
---------------
* https://pyvideo.org/pycon-au-2018/a-guided-tour-of-python-logging.html
* https://docs.python.org/3/howto/logging.html
* https://docs.python.org/3/library/logging.html#module-logging
* https://docs.python.org/3/library/logging.config.html#module-logging.config
* https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers


Logging Levels
==============
* Critical - Error, cannot continue
* Error - Error, can continue
* Warning - Warning, will do something important
* Info - I will do something
* Debug - This is how I am doing this


Default Level
-------------


Change Level
------------


Error vs Critical
-----------------
* Critical - not working, and cannot continue (fatal)
* Error - not working, but can continue (it is not fatal)


Logging Formatters
==================


General
-------
* ``name`` - Name of the logger used to log the call
* ``levelname`` - Text logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL)
* ``message`` - The logged message, computed as ``msg % args``. This is set when ``Formatter.format`` is invoked


Dates
-----
* ``asctime`` - Human-readable time when ``LogRecord`` was created, example: 1969-07-21 02:56:15,123
* ``created`` - Time when the ``LogRecord`` was created (as returned by ``time.time``)
* ``msecs`` - Millisecond portion of the time when the ``LogRecord`` was created


File and Module
---------------
* ``pathname`` - Full pathname of the source file where the logging call was issued (if available)
* ``filename`` - Filename portion of ``pathname``
* ``module`` - Module (name portion of ``filename``)
* ``funcName`` - Name of function containing the logging call
* ``lineno`` - Source line number where the logging call was issued (if available)


Process and Thread
------------------
* ``process`` - Process ID (if available)
* ``processName`` - Process name (if available)
* ``thread`` - Thread ID (if available)
* ``threadName`` - Thread name (if available)


Other
-----
* You shouldn't need to format this yourself
* ``args`` - The tuple of arguments merged into ``msg`` to produce ``message``, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary)
* ``exc_info`` - Exception tuple (à la ``sys.exc_info``) if no exception has occurred, ``None``
* ``msg`` - The format string passed in the original logging call. Merged with ``args`` to produce ``message``, or an arbitrary object
* ``stack_info`` - Stack frame information (where available) from the bottom of the stack in the current thread, up to and including the stack frame of the logging call which resulted in the creation of this record
* ``levelno`` - Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL)
* ``relativeCreated`` - Time in milliseconds when the ``LogRecord`` was created, relative to the time the logging module was loaded


Date Format
-----------


Log Style
---------
* ``{`` - curly brackets; compare to f-string formatting
* ``%`` - percent sign; compare to formatting string with ``%``
* ``$`` - dollar sign; compare to template vars from other languages
* Default mode is ``%`` percent


Logging Config Basic
====================
* ``filename`` - Specifies that a ``FileHandler`` be created, using the specified filename, rather than a ``StreamHandler``
* ``filemode`` - If filename is specified, open the file in this mode. Defaults to ``'a'``
* ``format`` - Use the specified format string for the handler
* ``datefmt`` - Use the specified date/time format, as accepted by ``time.strftime()``
* ``style`` - If format is specified, use this style for the format string. One of ``'%'``, ``'{'`` or ``'$'`` for printf-style, ``str.format()`` or ``string.Template`` respectively. Defaults to ``'%'``
* ``level`` - Set the root logger level to the specified level
* ``stream`` - Use the specified stream to initialize the ``StreamHandler``. Note that this argument is incompatible with ``filename`` - if both are present, a ``ValueError`` is raised
* ``handlers`` - If specified, this should be an iterable of already created handlers to add to the root logger. Any handlers which don't already have a formatter set will be assigned the default formatter created in this function. Note that this argument is incompatible with ``filename`` or ``stream`` - if both are present, a ``ValueError`` is raised


Logging Handlers
================
* https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers


Logging Config File
===================


File Config
-----------
* ``logging.config.fileConfig(fname, defaults=None, disable_existing_loggers=True, encoding=None)``
* https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig


``DictConfig``
--------------
* logging.config.dictConfig(config)
* https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
* https://docs.python.org/3/library/logging.config.html#dictionary-schema-details


Handlers
--------
* https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers


Rotate
------
* ``logging.handlers.WatchedFileHandler``
* ``logging.handlers.RotatingFileHandler``
* ``logging.handlers.TimedRotatingFileHandler``


Optimization
------------


Further Reading
---------------
* https://pyvideo.org/pycon-au-2018/a-guided-tour-of-python-logging.html
* https://docs.python.org/3/howto/logging.html
* https://docs.python.org/3/library/logging.html#module-logging
* https://docs.python.org/3/library/logging.config.html#module-logging.config
* https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers


Logging Rotation
================
* https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers


BaseRotatingHandler
-------------------
* ``logging.handlers.BaseRotatingHandler``


RotatingFileHandler
-------------------
* ``logging.handlers.RotatingFileHandler``


TimedRotatingFileHandler
------------------------
* ``logging.handlers.TimedRotatingFileHandler``


Logging Optimization
====================


Logging Use Cases
=================
