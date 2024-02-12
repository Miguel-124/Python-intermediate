"""
* Assignment: OOP AttributeMutability Randint
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. Create dataclass `Hero`, with attributes:
        a. `name: str` (required)
        b. `health: int` (optional), default: randint(50, 100)
    2. Attributes must be set at the initialization from constructor arguments
    3. Avoid mutable parameter problem
    4. Użyj funkcji `randint()` z biblioteki `random`
    5. Do not use `dataclass`
    6. Run doctests - all must succeed

Polish:
    1. Stwórz dataklasę `Hero`, z atrybutami:
        a. `name: str` (wymagane)
        b. `health: int` (opcjonalne), domyślnie: randint(50, 100)
    2. Atrybuty mają być ustawiane przy inicjalizacji z parametrów konstruktora
    3. Uniknij problemu mutowalnych parametrów
    4. Użyj funkcji `randint()` z biblioteki `random`
    5. Nie używaj `dataclass`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from random import seed; seed(0)

    >>> assert isclass(Hero)
    >>> assert hasattr(Hero, '__annotations__')

    >>> warrior = Hero('Warrior')
    >>> assert warrior.name == 'Warrior'
    >>> assert warrior.health == 74

    >>> mage = Hero('Mage')
    >>> assert mage.name == 'Mage'
    >>> assert mage.health == 98

    >>> rouge = Hero('Rouge')
    >>> assert rouge.name == 'Rouge'
    >>> assert rouge.health == 76

    >>> cleric = Hero('Cleric')
    >>> assert cleric.name == 'Cleric'
    >>> assert cleric.health == 52
"""
from random import randint


# Create class `User`, with attributes:
# - `name: str` (required)
# - `health: int` (optional), default: randint(50, 100)
# type: type[Hero]
class Hero:
    ...


