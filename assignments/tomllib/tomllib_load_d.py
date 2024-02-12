"""
* Assignment: TOML Load Authors
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Read configuration from `FILE`
    2. Define `result: datetime` with release date
    3. Use `tomllib.load()`
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj konfigurację z `FILE`
    2. Zdefiniuj `result: datetime` z datą wdrożenia
    3. Użyj `tomllib.load()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * open(filename, mode='rb')
    * import tomllib
    * tomllib.load()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from datetime import datetime
    >>> from os import remove
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is datetime, \
    'Variable `result` has invalid type, should be datetime'

    >>> pprint(result)
    datetime.datetime(2020, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)
"""
import datetime
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
"""

with open(FILE, mode='wb') as file:
    file.write(DATA)


# Read configuration from `FILE`
# Define `result: datetime` with release date
# type: dict[str, str|int]
with open(FILE, mode='rb') as file:
    result = tomllib.load(file)['metadata']['release_date']


