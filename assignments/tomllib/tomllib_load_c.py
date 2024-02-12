"""
* Assignment: TOML Load Stats
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Game characters stats are written to `FILE`
    2. Define function `get_stats(name: str) -> dict`
        a. Parameter `name: str`, example: 'Sarevok'
        b. Returns `dict` with character named `name` stats
    3. Use `tomllib.load()`
    4. Run doctests - all must succeed

Polish:
    1. Statystyki postaci z gry zapisano do `FILE`
    2. Zdefiniuj funkcję `get_stats(name: str) -> dict`
        a. Parametr `name: str`, przykład: 'Sarevok'
        b. Zwraca `dict` ze statystykami postaci o imieniu `name`
    3. Użyj `tomllib.load()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * open(filename, mode='rb')
    * import tomllib
    * tomllib.load()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> imoen = get_stats('Imoen')
    >>> assert imoen['character_class'] == 'Thief'
    >>> assert imoen['race'] == 'Human'
    >>> assert imoen['alignment'] == 'Neutral Good'
    >>> assert imoen['strength'] == 9
    >>> assert imoen['dexterity'] == 18
    >>> assert imoen['constitution'] == 16
    >>> assert imoen['intelligence'] == 17
    >>> assert imoen['wisdom'] == 11
    >>> assert imoen['charisma'] == 16

    >>> minsc = get_stats('Minsc')
    >>> assert minsc['character_class'] == 'Ranger'
    >>> assert minsc['race'] == 'Human'
    >>> assert minsc['alignment'] == 'Neutral Good'
    >>> assert minsc['strength'] == 18
    >>> assert minsc['dexterity'] == 15
    >>> assert minsc['constitution'] == 15
    >>> assert minsc['intelligence'] == 8
    >>> assert minsc['wisdom'] == 6
    >>> assert minsc['charisma'] == 9

    >>> neera = get_stats('Neera')
    >>> assert neera['character_class'] == 'Wild Mage'
    >>> assert neera['race'] == 'Half-elf'
    >>> assert neera['alignment'] == 'Chaotic Neutral'
    >>> assert neera['strength'] == 11
    >>> assert neera['dexterity'] == 17
    >>> assert neera['constitution'] == 14
    >>> assert neera['intelligence'] == 17
    >>> assert neera['wisdom'] == 10
    >>> assert neera['charisma'] == 11

    >>> sarevok = get_stats('Sarevok')
    >>> assert sarevok['character_class'] == 'Fighter'
    >>> assert sarevok['race'] == 'Human'
    >>> assert sarevok['alignment'] == 'Chaotic Evil'
    >>> assert sarevok['strength'] == 18
    >>> assert sarevok['dexterity'] == 17
    >>> assert sarevok['constitution'] == 18
    >>> assert sarevok['intelligence'] == 17
    >>> assert sarevok['wisdom'] == 10
    >>> assert sarevok['charisma'] == 15

    >>> remove(FILE)
"""
import tomllib
from dataclasses import dataclass
from pathlib import Path
from random import randint
from typing import NamedTuple

FILE = '_temporary.toml'

DATA = b"""
[Imoen]
character_class = 'Thief'
race = 'Human'
alignment = 'Neutral Good'
strength = 9
dexterity = 18
constitution = 16
intelligence = 17
wisdom = 11
charisma = 16

[Minsc]
character_class = 'Ranger'
race = 'Human'
alignment = 'Neutral Good'
strength = 18
dexterity = 15
constitution = 15
intelligence = 8
wisdom = 6
charisma = 9

[Neera]
character_class = 'Wild Mage'
race = 'Half-elf'
alignment = 'Chaotic Neutral'
strength = 11
dexterity = 17
constitution = 14
intelligence = 17
wisdom = 10
charisma = 11

[Sarevok]
character_class = 'Fighter'
race = 'Human'
alignment = 'Chaotic Evil'
strength = 18
dexterity = 17
constitution = 18
intelligence = 17
wisdom = 10
charisma = 15
"""

with open(FILE, mode='wb') as file:
    file.write(DATA)


# Game characters stats are written to `FILE`
# Define function `get_stats(name: str) -> dict`
#  a. Parameter `name: str`, example: 'Sarevok'
#  b. Returns `dict` with character named `name` stats
# Use `tomllib.load()`
# type: Callable[[str], dict]
def get_stats(name: str) -> dict:
    with open(FILE, mode='rb') as file:
        config = tomllib.load(file)
        return config[name]
