"""
* Assignment: TOML Load Authors
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Read configuration from `FILE`
    2. Define `result: list[str]` with author emails
    3. Use `tomllib.load()`
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj konfigurację z `FILE`
    2. Zdefiniuj `result: list[str]` z adresami email autorów
    3. Użyj `tomllib.load()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * open(filename, mode='rb')
    * import tomllib
    * tomllib.load()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from os import remove
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'

    >>> result = sorted(result)
    >>> pprint(result)
    ['avogel@nasa.gov',
     'bjohanssen@nasa.gov',
     'cbeck@nasa.gov',
     'mlewis@nasa.gov',
     'mwatney@nasa.gov',
     'rmartinez@nasa.gov']
"""
import tomllib
from dataclasses import dataclass
from pathlib import Path
from random import randint
from typing import NamedTuple

FILE = '_temporary.toml'

DATA = b"""
project = 'My App'
version = '1.0.0'

[database]
hostname = '127.0.0.1'
port = 5432
username = 'mwatney'
password = 'Ares3'
database = 'nasa'

[metadata]
release_date = 2020-01-01T00:00:00Z
authors = [
    { name = 'Mark Watney', email = 'mwatney@nasa.gov' },
    { name = 'Melisa Lewis', email = 'mlewis@nasa.gov' },
    { name = 'Rick Martinez', email = 'rmartinez@nasa.gov' },
    { name = 'Alex Vogel', email = 'avogel@nasa.gov' },
    { name = 'Beth Johanssen', email = 'bjohanssen@nasa.gov' },
    { name = 'Chris Beck', email = 'cbeck@nasa.gov' },
]
"""

with open(FILE, mode='wb') as file:
    file.write(DATA)


# Read configuration from `FILE`
# Define `result: list[str]` with author emails
# type: dict[str, str|int]
with open(FILE, mode='rb') as file:
    result = [author['email'] for author in tomllib.load(file)['metadata']['authors']]
