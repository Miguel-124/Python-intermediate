

Datetime Create
===============
* Date
* Time
* Datetime


Custom Date and Time
--------------------


Date Attributes
---------------


Time Attributes
---------------


Datetime Attributes
-------------------


Current Date and Time
---------------------


Combine
-------


Split
-----


Empty Time
----------


Datetime ISO Standard
=====================
* ISO 8601 is an International Standard [#wikiISO8601]_


Dates
-----
* Year-Month-Day
* Format: ``YYYY-mm-dd``
* Example: 1969-07-21


Time
----
* 24 hour clock
* Format: ``HH:MM:SS.ffffff`` or ``HH:MM:SS`` or ``HH:MM``
* Example: 12:34, 12:34:56, 12:34:56.123456
* Optional seconds and microseconds
* ``00:00`` - midnight, at the beginning of a day
* ``24:00`` - midnight, at the end of a day (not recommended)
* ``1969-12-31T24:00`` is equal to ``1970-01-01T00:00``


Date and Time
-------------
* Format: ``YYYY-mm-ddTHH:MM:SS.ffffff``
* Example: 1961-04-12T06:07:00.123456
* "T" separates date and time)
* Optional seconds and microseconds


Timezone
--------
* Format: ``YYYY-mm-ddTHH:MM:SS.ffffffUTC``
* Format: ``YYYY-mm-ddTHH:MM:SS.ffffffZ``
* Example: 1961-04-12T06:07:00.123456+0200
* Optional seconds and microseconds
* "Z" (Zulu) means UTC


Week
----
* Format: ``YYYY-Www``
* The ISO 8601 definition for week 01 is the week with the first Thursday of the Gregorian year (i.e. of January) in it. [#wikisoweekdate]_
* ``2009-W01`` - First week of 2009
* ``2009-W53`` - Last week of 2009


Weekday
-------
* Format: ``YYYY-Www-dd``
* Week starts on Monday
* ISO defines Monday as one
* Note year/month changes during the week
* ``2009-W01-1`` - Monday 29 December 2008
* ``2009-W53-7`` - Sunday 3 January 2010


Duration
--------
* Format: ``P...Y...M...DT...H...M...S``
* Example: P8Y3M8DT20H49M15S
* ``P`` - period - placed at the start of the duration representation
* ``Y`` - number of years
* ``M`` - number of months
* ``W`` - number of weeks
* ``D`` - number of days
* ``T`` - precedes the time components of the representation
* ``H`` - number of hours
* ``M`` - number of minutes
* ``S`` - number of seconds


To ISO Format
-------------
* ``datetime.isoformat()``
* ``date.isoformat()``
* ``time.isoformat()``


From ISO Format
---------------
* ``datetime.fromisoformat()``
* ``date.fromisoformat()``
* ``time.fromisoformat()``


Datetime Standards
==================
* Date and time formats varies from country to country [#wikiDateTimeFormats]_


Date
----


24 Hour Clock
-------------


12 Hour Clock
-------------
* What AM stands for?
* What PM stands for?


Noon and Midnight
-----------------
* Confusion at noon and midnight [#wikiNoonMidnight]_
* Which time is a midnight?
* Which time is a noon?


Exactly Midnight
----------------
* ``00:00:00.000000`` - day start, exactly midnight
* ``23:59:59.999999`` - day end, excluding last microsecond
* ``24:00:00.000000`` - day end, including last microsecond


After Midnight
--------------
* Times after Midnight [#wikiTimesAfter2400]_


Leap Second
-----------
* UTC leap second [#wikiLeapSecond]_
* Leap second discontinuation post 2035 [#natureLeapSecond]_
* Issues created by insertion (or removal) of leap seconds
* Calculation of time differences and sequence of events
* Missing leap seconds announcement
* Implementation differences
* Textual representation of the leap second
* Binary representation of the leap second
* Other reported software problems associated with the leap second
* June 30th or December 31st
* Introduced in 1972
* Last leap second in 2016


Zero Padded
-----------
* Zero padded minutes, seconds and microseconds but not hours
* Variable length microseconds


Roman Numerals
--------------
* In latin ``V`` is read as ``U``
* In latin ``I`` is read as ``J``
* In latin ``IV`` is read as ``JU``
* ``JU`` stands for Jupyter - roman god
* Louis XIV did not like ``IV`` and changed to ``IIII`` [#watchmaster]_
* There is a symetry in groups of four ``I, II, III, IIII``, ``V, VI, VII, VIII``, ``IX, X, XI, XII``


Military Time
-------------
* Military time [#wikiMilitaryTime]_
* Military time zones [#wikiMilitaryTimezones]_
* 24 hour clock


Decimal Time
------------
* Unix time gives date and time as the number of seconds since January 1, 1970
* Microsoft's FILETIME as multiples of 100ns since January 1, 1601 [#wikiMetricTime]_
* VAX/VMS uses the number of 100ns since November 17, 1858 [#wikiMetricTime]_
* RISC OS the number of centiseconds since January 1, 1900 [#wikiMetricTime]_


Other
-----
* Swatch Internet Time - Beats @300 [#wikiSwatchInternetTime]_
* sidereal day on Earth is approximately 86164.0905 seconds (23 h 56 min 4.0905 s or 23.9344696 h)


Calendars
---------
* Julian Calendar [#wikiJulianCalendar]_
* Gregorian Calendar [#wikiGregorianCalendar]_
* Introduced by Pope Gregory XIII in October 1582
* Saudi Arabia was the last country to adopt Gregorian calendar in 2016
* There are only four countries which have not adopted the Gregorian calendar: Ethiopia (Ethiopian calendar), Nepal (Vikram Samvat and Nepal Sambat), Iran and Afghanistan (Solar Hijri calendar)
* List of adoption dates of the Gregorian calendar by country [#wikiGregorianCalendarAdoption]_


Astronomy
---------
* Synodic day - the period for a celestial object to rotate once in relation to the star it is orbiting [#wikiSynodicDay]_
* Solar time - calculation of the passage of time based on the position of the Sun in the sky [#wikiSolarTime]_
* Epoch (astronomy) [#wikiEpochAstronomy]_
* Sidereal Time [#wikiSiderealTime]_
* JD - Julian Day [#wikiJulianDay]_


Space Industry
--------------
* UTC - Coordinated Universal Time [#wikiCoordinatedUniversalTime]_
* GMT - Greenwich Mean Time [#wikiGreenwichMeanTime]_
* MET - Mission Elapsed Time
* Relativistic effects
* Time dilatation due to speed approaching speed of light


Planet Mars
-----------
* MSD - Mars Sol Date [#wikiMarsSolDate]_
* MTC - Coordinated Mars Time [#wikiCoordinatedMarsTime]_
* Timekeeping on Mars [#wikiTimekeepingOnMars]_
* Mars Clock [#wikiMarsClock]_
* Martian sidereal day is 24 h 37 m 22.663 s (88,642.663 seconds)
* Martian solar day is 24 h 39 m 35.244 s (88,775.244 seconds)


Datetime Format
===============
* ``format(dt, '%Y-%m-%d')``
* ``f'Today is {dt:%Y-%m-%d}'``
* ``dt.strftime('%Y-%m-%d')``


Formats
-------
* ``format(dt, '%Y-%m-%d')``


Parameters
----------
* Similar in almost all programming language
* Some minor differences like in JavaScript minutes are ``i``, not ``M``


Leading Zero
------------
* ``%#H`` - remove leading zero (Windows)
* ``%-H`` - remove leading zero (macOS, Linux, \*nix)
* ``%_H`` - replace leading zero with space (macOS, Linux, \*nix)
* Works only with formatting
* raises ValueError while parsing [#pydocdtformat]_


String Format Time
------------------
* ``datetime.strftime()``


Format String
-------------


Datetime Parse
==============
* Parsing - analyze (a sentence) into its parts and describe their syntactic roles.


Parsing dates
-------------


Leading Zero
------------


String Fitting
--------------


Time Zone
---------
* More information in `Datetime Timezone`


Parsing Parameters
------------------


Datetime Timedelta
==================


Timedelta object
----------------


Simple Time Shift
-----------------


Complex Shifts
--------------


Month Shifts
------------


Duration
--------
* Period between two datetimes


Further Reading
---------------
* https://dateutil.readthedocs.io/en/stable/examples.html
* https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html


Datetime Timestamp
==================


What is timestamp?
------------------
* Seconds since midnight of January 1st, 1970 (1970-01-01 00:00:00 UTC)
* Unix era, also known as "epoch"
* In most systems represented as 32-bit integer
* Max value is 2,147,483,647 (2038-01-19 03:14:07 UTC)
* Min value is -2,147,483,647 (1901-12-13 20:45:52 UTC)
* If you add 1 to max value, you will get overflow to min value
* Linux kernel 5.6 (released 29 March 2020) has a fix for this problem so that 32-bit systems can run beyond the year 2038
* https://itsfoss.com/linux-kernel-5-6/
* https://lore.kernel.org/lkml/CAHk-=wi9ZT7Stg-uSpX0UWQzam6OP9Jzz6Xu1CkYu1cicpD5OA@mail.gmail.com/
* https://en.wikipedia.org/wiki/Year_2038_problem
* Excel error: https://learn.microsoft.com/en-US/office/troubleshoot/excel/wrongly-assumes-1900-is-leap-year


Get current timestamp
---------------------


Convert timestamp to ``datetime``
---------------------------------


Datetime Time Utils
===================


Sleep
-----


``calendar``
------------
* HTML Calendar


Datetime Timezone
=================
* Always keep dates and times only in UTC (**important!**)
* Datetimes should be converted to local time only when displaying to user
* Computerphile Time & Time Zones [#ytComputerphileTimeZones]_
* Abolition of Time Zones [#wikiAbolitionOfTimeZones]_
* Since Python 3.9: :pep:`615` -- Support for the IANA Time Zone Database in the Standard Library
* ``pip install tzdata``


Daylight Saving Time
--------------------
* Daylight Saving Time date is different for each country and even US state
* Australia is 9h 30m shifted
* India is 3h 30m shifted
* Nepal is 3h 45m shifted
* In southern hemisphere the Daylight Saving Time is opposite direction
* They subtract hour in March and add in October
* Samoa is on the international date line
* Samoa changed from UTC-1200 to UTC+1200 for easier trades with Australia
* During World War II England was GMT+0200
* Libya in 2013 discontinued DST with couple of days notice
* Israel is on a different timezone than Palestine (multiple timezones in one location, based on nationality)
* Change from Julian to Gregorian calendar caused to skip few weeks
* In 18th century World change from Julian to Gregorian calendar
* In 20th century Russia change from Julian to Gregorian calendar (different days which was skipped than for worldwide change)
* In britain until 16th century the year started on 25th of March
* Mind leap seconds (add, subtract)
* UTC includes leap seconds
* Astronomical time does not include leap seconds
* Google invented smear second (on the day of leap second) they add a small fraction of a second to each second that day until midnight
* Not all cities has DST https://www.timeanddate.com/time/us/arizona-no-dst.html


Timezone Naive Datetimes
------------------------


Timezone Aware Datetimes
------------------------


UTCNow
------
* ``datetime.utcnow()`` produces timezone naive datetimes!


IANA Time Zone Database
-----------------------
* https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
* https://www.iana.org/time-zones
* https://pypi.org/project/tzdata/
* https://en.wikipedia.org/wiki/Time_in_Antarctica
* ``pip install tzdata``


ZoneInfo
--------
* Since Python 3.9: :pep:`615` -- Support for the IANA Time Zone Database in the Standard Library
* https://docs.python.org/3/library/zoneinfo.html
