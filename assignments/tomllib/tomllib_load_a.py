"""
* Assignment: TOML Load Version
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Read configuration from `FILE`
    2. Define `result: dict` with version read from config
    3. Use `tomllib.load()`
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj konfigurację z `FILE`
    2. Zdefiniuj `result: dict` z werją wczytaną z konfiguracji
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
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> pprint(result)
    '1.0.0'
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
"""

with open(FILE, mode='wb') as file:
    file.write(DATA)


# Read configuration from `FILE`
# Define `result: dict` with database config

# type: dict[str, str|int]
with open(FILE, mode='rb') as file:
    result = tomllib.load(file).get('version')

