

Regex Syntax About
==================
* Also known as ``Regular Expressions``
* Also known as ``Regular Expr``
* Also known as ``regexp``
* Also known as ``regex``
* Also known as ``re``
* https://www.youtube.com/watch?v=BmF-gEYXWVM&list=PLv4THqSPE6meFeo_jNLgUVKkP40UstIQv&index=3
* W3C HTML Email pattern: ``r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"``


Syntax
------
* Identifiers - what to find (single character)
* Qualifiers - range to find (range)
* Negation
* Quantifiers - how many occurrences of preceding qualifier or identifier
* Groups
* Look Ahead and Look Behind
* Flags
* Extensions
* ``[]`` - Qualifier
* ``{}`` - Quantifier
* ``()`` - Groups


Escape characters
-----------------
* Escape characters
* ``\t`` - tab
* ``\r`` - carriage return
* ``\n`` - newline
* ``\r\n`` - newline (on Windows)
* ``\b`` - backspace
* ``\v`` - vertical space
* ``\f`` - form feed
* ``\x`` - hexadecimal
* ``\o`` - octal
* ``\u`` - Unicode entity 16-bit
* ``\U`` - Unicode entity 32-bit
* ``\\`` - backslash
* ``\'`` - apostrophe
* ``\"`` - double quote


String Modifiers
----------------


Raw Strings
-----------
* Recap information about raw strings ``r'...'``
* Since Python 3.12 ``r-string`` is required https://docs.python.org/dev/whatsnew/3.12.html#other-language-changes


ASCII vs Unicode
----------------
* ``re.UNICODE``
* ``re.ASCII``
* ASCII for letters in latin alphabet
* UNICODE includes diacritics and accent characters (ąśćłóźć, etc.)


Digit, Hexadecimal, Octal
-------------------------


Punctuation
-----------


Visualization
-------------
* https://regexper.com/
* https://regex101.com/


Further Reading
---------------
* https://www.youtube.com/watch?v=BmF-gEYXWVM&list=PLv4THqSPE6meFeo_jNLgUVKkP40UstIQv&index=3
* Kinsley, Harrison "Sentdex". Python 3 Programming Tutorial - Regular Expressions / Regex with re. Year: 2014. Retrieved: 2021-04-11. URL: https://www.youtube.com/watch?v=sZyAn2TW7GY
* https://www.rexegg.com/regex-trick-conditional-replacement.html
* https://www.rexegg.com/regex-lookarounds.html
* https://www.rexegg.com/regex-anchors.html#z


Regex Syntax Qualifier
======================
* Qualifier specifies what to find.
* ``a`` - Exact
* ``a|b`` - Alternative
* ``[abc]`` - Enumeration
* ``[a-z]`` - Range


Exact
-----
* ``a`` - Exact


Exact Alternate
---------------
* ``a|b`` - letter `a` or `b` (also works with expressions)


Enumeration
-----------
* ``[abc]`` - letter `a` or `b` or `c`


Range
-----
* ``[a-z]`` - any lowercase ASCII letter from `a` to `z`
* ``[A-Z]`` - any uppercase ASCII letter from `A` to `Z`
* ``[0-9]`` - any digit from `0` to `9`
* ``[a-zA-Z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[A-z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[a-zA-Z0-9]`` - any ASCII letter from `a` to `z` or from `A` to `Z` or digit from `0` to `9`


Joining
-------
* ``[abc]|[123]`` - Enumeration alternative - letter `a`, `b` or `c` or digit `1`, `2` `3`
* ``[a-z]|[0-9]`` - Range alternative - any lowercase ASCII letter from `a` to `z` or digit from `0` to `9`


Regex Syntax Anchor
===================
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)
* ``^`` - start of line (changes meaning with ``re.MULTILINE``)
* ``$`` - end of line (changes meaning with ``re.MULTILINE``)
* ``\A`` - start of text (doesn't change meaning with ``re.MULTILINE``)
* ``\Z`` - end of text (doesn't change meaning with ``re.MULTILINE``)


Any Character
-------------
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)


Start of Line
-------------
* ``^`` - start of a line
* Changes meaning with ``re.MULTILINE``


End of Line
-----------
* ``$`` - end of line
* Changes meaning with ``re.MULTILINE``


Start of String
---------------
* ``\A`` - start of a text
* Doesn't change meaning with ``re.MULTILINE``


End of String
-------------
* ``\Z`` - end of a text
* Doesn't change meaning with ``re.MULTILINE``


Regex Syntax Negation
=====================
* Negation logically inverts qualifier
* ``[^...]`` - anything but ...


Syntax
------
* ``[^...]`` - anything but ...


Compare
-------


Regex Syntax Identifier
=======================
* Identifiers specifies what to find
* They are also called Character Classes


Numeric
-------
* ``\d`` - digit
* ``\D`` - anything but digit


Whitespaces
-----------
* ``\s`` - whitespace (space, tab, newline, non-breaking space)
* ``\S`` - anything but whitespace
* ``\n`` - newline
* ``\r\n`` - windows newline
* ``\r`` - carriage return
* ``\b`` - backspace
* ``\t`` - tab
* ``\v`` - vertical space
* ``\f`` - form feed


Word Boundary
-------------
* Matches the empty string, but only at the beginning or end of a word
* ``\b`` - word boundary
* ``\B`` - anything but word boundary


Word Character
--------------
* ``\w`` - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
* ``\W`` - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)
* lowercase letters including diacritics (i.e. ąćęłńóśżź...) and accents
* uppercase letters including diacritics (i.e. ĄĆĘŁŃÓŚŻŹ...) and accents
* digits
* underscores ``_``


Regex Syntax Quantifier
=======================
* Quantifier specifies how many occurrences of preceding qualifier or identifier
* Exact
* Greedy
* Lazy


Exact
-----
* Exact match
* ``{n}`` - exactly `n` repetitions


Greedy
------
* Prefer longest matches
* Works better with numbers
* Not that good results for text
* Default behavior
* ``{n,m}`` - minimum `n` repetitions, maximum `m` times, prefer longer
* ``{,n}`` - maximum `n` repetitions, prefer longer
* ``{n,}`` - minimum `n` repetitions, prefer longer
* ``{0,1}`` - minimum 0 repetitions, maximum 1 repetitions (maybe)
* ``*`` - minimum 0 repetitions, no maximum, prefer longer (alias to ``{0,}``)
* ``+`` - minimum 1 repetitions, no maximum, prefer longer (alias to ``{1,}``)
* ``?`` - minimum 0 repetitions, maximum 1 repetitions, prefer longer (alias to ``{0,1}``)


Lazy
----
* Prefer shortest matches
* Works better with text
* Not that good results for numbers
* Non-greedy
* ``{n,m}?`` - minimum `n` repetitions, maximum `m` times, prefer shorter
* ``{,n}?`` - maximum `n` repetitions, prefer shorter
* ``{n,}?`` - minimum `n` repetitions, prefer shorter
* ``{0,1}?`` - minimum 0 repetitions, maximum 1 repetitions (maybe)
* ``*?`` - minimum 0 repetitions, no maximum, prefer shorter (alias to ``{0,}?``)
* ``+?`` - minimum 1 repetitions, no maximum, prefer shorter (alias to ``{1,}?``)
* ``??`` - minimum 0 repetitions, maximum 1 repetition, prefer shorter (alias to ``{0,1}?``)


Greedy vs. Lazy
---------------


Regex Syntax Group
==================
* Catch expression results
* Can be named or positional
* Note, that for backreference, must use raw-sting or double backslash
* ``()`` - matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
* ``(...)`` - unnamed group
* ``(?P<mygroup>...)`` - named group `mygroup`
* ``(?:...)`` - non-capturing group
* ``(?#...)`` - comment


Positional Group
----------------
* ``(...)`` - unnamed (positional) group


Named Group
-----------
* ``(?P<mygroup>...)`` - named group `mygroup`


Non-Capturing Group
-------------------
* ``(?:...)``


Comment
-------
* ``(?#...)`` - comment


Backreference
-------------
* ``\g<number>`` - backreferencing by group number
* ``\g<name>`` - backreferencing by group name
* ``(?P=name)`` - backreferencing by group name
* ``\number`` - backreferencing by group number


Regex Syntax Flag
=================
* ``re.ASCII`` - perform ASCII-only matching instead of full Unicode matching
* ``re.IGNORECASE`` - case-insensitive search
* ``re.LOCALE`` - case-insensitive matching dependent on the current locale (deprecated)
* ``re.MULTILINE`` - match can start in one line, and end in another
* ``re.DOTALL`` - dot (``.``) matches also newline characters
* ``re.UNICODE`` - turns on unicode character support for ``\w``
* ``re.VERBOSE`` - ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``
* ``re.DEBUG`` - display debugging information during pattern compilation


ASCII
-----
* Short: ``a``
* Long: ``re.ASCII``
* Perform ASCII-only matching instead of full Unicode matching
* Works for ``\w``, ``\W``, ``\b``, ``\B``, ``\d``, ``\D``, ``\s`` and ``\S``
* ASCII only search is faster, but does not include unicode characters


IGNORECASE
----------
* Short: ``i``
* Long: ``re.IGNORECASE``
* Case-insensitive search
* Has Unicode support i.e. ``Ą`` and ``ą``


LOCALE
------
* Short: ``L``
* Long: ``re.LOCALE``
* Case-insensitive matching dependent on the current locale
* Work for ``\w``, ``\W``, ``\b``, ``\B``
* Use of this flag is discouraged as the locale mechanism is very unreliable
* It only works with 8-bit locales


MULTILINE
----------
* Short: ``m``
* Long: ``re.MULTILINE``
* Match can start in one line, and end in another
* Changes meaning of ``^``, now it is a start of a line
* Changes meaning of ``$``, now it is an end of line


DOTALL
------
* Short: ``s``
* Long: ``re.DOTALL``
* Dot (``.``) matches also newline characters
* By default newlines are not matched by ``.``


UNICODE
-------
* Short: ``u``
* Long: ``re.UNICODE``
* On by default
* Turns on unicode character support
* Works for ``\w`` and ``\W``


VERBOSE
-------
* Short: ``x``
* Long: ``re.VERBOSE``
* Ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``


DEBUG
-----
* Long: ``re.DEBUG``
* Display debugging information during pattern compilation


Regex Syntax Look Ahead/Behind
==============================


Syntax
------
* ``(?=)`` - Lookahead
* ``(?<=)`` - Lookbehind
* ``(?!foo)`` - Negative Lookahead
* ``(?<!foo)`` - Negative Lookbehind
* ``\K`` - Stop Look Behind


Regex Syntax Flavors
====================
* In other programming languages
* PCRE - Perl Compatible Regular Expressions


Future
------
* Since Python 3.11
* Atomic grouping ``((?>...))`` and possessive quantifiers (``*+``, ``++``, ``?+``, ``{m,n}+``) are now supported in regular expressions.
* https://www.regular-expressions.info/atomic.html
* https://github.com/python/cpython/issues/34627


Enclosing
---------
* In Python we use raw-string (``r'...'``)
* In JavaScript we use ``/pattern/flags`` or ``new RegExp(pattern, flags)``


Flags
-----
* In Python we use raw-string (``r'...'``)
* In JavaScript we use ``/pattern/flags`` or ``new RegExp(pattern, flags)``


Named Ranges
------------
* ``[:allnum:]`` - Alphabetic and numeric character ``[a-zA-Z0-9]``
* ``[:alpha:]`` - Alphabetic character ``[a-zA-Z]``
* ``[:alnum:]`` - Alphabetic and numeric character ``[a-zA-Z0-9]``
* ``[:alpha:]`` - Alphabetic character ``[a-zA-Z]``
* ``[:blank:]`` - Space or tab
* ``[:cntrl:]`` - Control character
* ``[:digit:]`` - Digit
* ``[:graph:]`` - Non-blank character (excludes spaces, control characters, and similar)
* ``[:lower:]`` - Lowercase alphabetical character
* ``[:print:]`` - Like [:graph:], but includes the space character
* ``[:punct:]`` - Punctuation character
* ``[:space:]`` - Whitespace character (``[:blank:]``, newline, carriage return, etc.)
* ``[:upper:]`` - Uppercase alphabetical
* ``[:xdigit:]`` - Digit allowed in a hexadecimal number (i.e., 0-9a-fA-F)
* ``[:word:]`` - A character in one of the following Unicode general categories Letter, Mark, Number, Connector_Punctuation
* ``[:ascii:]`` - A character in the ASCII character set


Range
-----
* ``[a-Z]`` == ``[a-zA-Z]``
* ``[a-9]`` == ``[a-zA-Z0-9]``
* Works in other languages, but not in Python


Group Backreference
-------------------
* ``$1`` - grep, egrep, Jetbrains IDE
* ``\1``
* ``\g<1>`` - Python
* ``\g<name>`` - Python


Regex Syntax Use Cases
======================


National Identification Numbers
-------------------------------
* Worldwide
* https://github.com/arthurdejong/python-stdnum/tree/master/stdnum/pl


Dates
-----


Email
-----
* [#rfc3696]_


URL
---


Parsing URLs
------------
* Source [#W3CParsingURLs]_


Regex Recap
===========


Literals
--------
* Also known as "Literal Characters"
* Occurrence of that character in the string


Classes
-------
* Also known as "Character Classes"
* One out of several characters


Metacharacters
--------------
* Special characters


Anchors
-------
* Match a position before, after, or between characters


Negation
--------
* Negation logically inverts qualifier


Shorthands
----------
* Shorthand Character Classes


Quantifiers
-----------
* Repetition
* How many occurrences of preceding token
* Exact - exactly number of times
* Greedy - prefer longest match, works better with numbers, (default)
* Lazy - prefer shortest matches - works better with text


Groups
------
* Catch expression results
* Can be named or positional


Backreference
-------------
* Match the same text as previously matched by a capturing group


Flags
-----
* ``re.ASCII`` - perform ASCII-only matching instead of full Unicode matching
* ``re.IGNORECASE`` - case-insensitive search
* ``re.LOCALE`` - case-insensitive matching dependent on the current locale (deprecated)
* ``re.MULTILINE`` - match can start in one line, and end in another
* ``re.DOTALL`` - dot (``.``) matches also newline characters
* ``re.UNICODE`` - turns on unicode character support for ``\w``
* ``re.VERBOSE`` - ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``
* ``re.DEBUG`` - display debugging information during pattern compilation


Python
------
* ``re.findall()`` - all matches at once, returns ``list[str]``
* ``re.finditer()`` - all matches one at a time, returns ``Iterator[re.Match]``
* ``re.search()`` - whether text contains (stop after first match), returns ``re.Match | None``
* ``re.match()`` - whether text matches pattern (validation, np. email, ssn, tax id, phone), returns ``re.Match | None``
* ``re.split()`` - splits text by pattern, returns ``list[str]``
* ``re.sub()`` - replaces group matches in text (works best with named groups), returns ``str``
* ``re.compile()`` - prepares pattern for further use (match against it), returns ``re.Pattern``


Regex RE Match
==============
* ``re.match()``
* Checks exact match
* Checking if user input is correct (email, url, NIP, VAT ID, PESEL)


Good Practices
--------------
* Doctests


Doctests
--------


Regex RE Search
===============
* ``re.search()``
* Searches if pattern contains a string


Regex RE Findall, Finditer
==========================
* ``re.findall()``
* ``re.finditer()``


Regex RE Compare
================
* ``re.match()``
* ``re.search()``
* ``re.findall()``


Regex RE Compile
================
* ``re.compile()``
* Used when pattern is reused (especially in the loop)


Syntax
------


No Compile
----------


Compile
-------


Regex RE Group
==============
* Match particular parts of a string
* Possible to name matches


Syntax
------


Positional Groups
-----------------


Named Groups
------------
* Usage of group in ``re.match()``


Non-Capturing Groups
--------------------


Regex RE Multiline
==================
* ``re.MULTILINE`` - Flag turns on Multiline search
* ``^`` - Matches the start of the string, and immediately after each newline
* ``$`` - Matches the end of the string or just before the newline at the end of the string also matches before a newline


Regex RE Substitute
===================
* ``re.sub()``
* Replace matched substring with text


Regex RE Split
==============
* ``re.split()``
* Split text by pattern


Regex RE Lazy
=============
* Adding ``?`` after the qualifier makes it non-greedy
* Greedy - as many as possible
* Lazy - as few as possible:
* ``?`` - zero or one (greedy)
* ``*`` - zero or more (greedy)
* ``+`` - one or more (greedy)
* ``??`` - zero or one (lazy)
* ``*?`` - zero or more (lazy)
* ``+?`` - one or more (lazy)


Regex RE Type Annotation
========================
* ``typing.Pattern``
* ``typing.Match``


Regex Cheatsheet
================
* Also known as: "Regular Expressions", "Regular Expr", "regexp", "regex" or "re"
* ``a`` - exact
* ``a|b`` - alternative
* ``[abc]`` - enumerated character class
* ``[a-z]`` - range character class
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)
* ``^`` - start of line (changes meaning with ``re.MULTILINE``)
* ``$`` - end of line (changes meaning with ``re.MULTILINE``)
* ``\A`` - start of text (doesn't change meaning with ``re.MULTILINE``)
* ``\Z`` - end of text (doesn't change meaning with ``re.MULTILINE``)
* ``[^]`` - negation
* ``\d`` - digit (alias to ``[0-9]``)
* ``\D`` - anything but digit (alias to ``[^0-9]``)
* ``\s`` - whitespace (space, tab, newline, non-breaking space)
* ``\S`` - anything but whitespace
* ``\b`` - word boundary
* ``\B`` - anything but word boundary
* ``\w`` - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
* ``\W`` - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)
* ``{n}`` - exactly `n` repetitions, exact
* ``{,n}`` - maximum `n` repetitions, greedy (prefer longest)
* ``{n,}`` - minimum `n` repetitions, greedy (prefer longest)
* ``{n,m}`` - minimum `n` repetitions, maximum `m` times, greedy (prefer longest)
* ``*`` - minimum 0 repetitions, no maximum, greedy (prefer longest), alias to ``{0,}``
* ``+`` - minimum 1 repetitions, no maximum, greedy (prefer longest), alias to ``{1,}``
* ``?`` - minimum 0 repetitions, maximum 1 repetitions, greedy (prefer longest), alias to ``{0,1}``
* ``{,n}?`` - maximum `n` repetitions, lazy (prefer shorter)
* ``{n,}?`` - minimum `n` repetitions, lazy (prefer shorter)
* ``{n,m}?`` - minimum `n` repetitions, maximum `m` times, lazy (prefer shorter)
* ``*?`` - minimum 0 repetitions, no maximum, lazy (prefer shorter), alias to ``{0,}?``
* ``+?`` - minimum 1 repetitions, no maximum, lazy (prefer shorter), alias to ``{1,}?``
* ``??`` - minimum 0 repetitions, maximum 1 repetition, lazy (prefer shorter), alias to ``{0,1}?``
* ``()`` - matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
* ``(...)`` - unnamed group (positional)
* ``(?P<mygroup>...)`` - named group `mygroup`
* ``(?:...)`` - non-capturing group
* ``(?#...)`` - comment
* ``(?P=name)`` - backreferencing by group name
* ``\g<number>`` - backreferencing by group number
* ``\g<name>`` - backreferencing by group name
* ``re.ASCII`` - perform ASCII-only matching instead of full Unicode matching
* ``re.IGNORECASE`` - case-insensitive search
* ``re.LOCALE`` - case-insensitive matching dependent on the current locale (deprecated)
* ``re.MULTILINE`` - match can start in one line, and end in another
* ``re.DOTALL`` - dot (``.``) matches also newline characters
* ``re.UNICODE`` - turns on unicode character support for ``\w``
* ``re.VERBOSE`` - ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``
* ``re.DEBUG`` - display debugging information during pattern compilation
