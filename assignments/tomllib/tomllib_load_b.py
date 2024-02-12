"""
* Assignment: TOML Load Database
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Read configuration from `FILE`
    2. Define `result: dict` with database config
    3. Use `tomllib.load()`
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj konfigurację z `FILE`
    2. Zdefiniuj `result: dict` z konfiguracją bazy danych
    3. Użyj `tomllib.load()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * open(filename, mode='rb')
    * import tomllib
    * tomllib.load()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert result['hostname'] == '127.0.0.1'
    >>> assert result['port'] == 5432
    >>> assert result['username'] == 'mwatney'
    >>> assert result['password'] == 'Ares3'
    >>> assert result['database'] == 'nasa'

    >>> remove(FILE)
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
"""

with open(FILE, mode='wb') as file:
    file.write(DATA)


# Read configuration from `FILE`
# Define `result: dict` with database config
# type: dict[str, str|int]
with open(FILE, mode='rb') as file:
    result = tomllib.load(file).get('database')

