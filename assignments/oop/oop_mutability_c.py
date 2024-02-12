"""
* Assignment: OOP AttributeMutability Dataclass list[str]
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create dataclass `User`, with attributes:
        a. `firstname: str` (required)
        b. `lastname: str` (required)
        c. `groups: list[str]` (optional), default: ['user']
    2. Attributes must be set at the initialization from constructor arguments
    3. Avoid mutable parameter problem
    4. Run doctests - all must succeed

Polish:
    1. Stwórz dataklasę `User`, z atrybutami:
        a. `firstname: str` (wymagane)
        b. `lastname: str` (wymagane)
        c. `groups: list[str]` (opcjonalne), domyślnie: ['user']
    2. Atrybuty mają być ustawiane przy inicjalizacji z parametrów konstruktora
    3. Uniknij problemu mutowalnych parametrów
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * field(default_factory=lambda: [...])

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert hasattr(User, '__annotations__')

    >>> assert 'firstname' in User.__dataclass_fields__
    >>> assert 'lastname' in User.__dataclass_fields__
    >>> assert 'groups' in User.__dataclass_fields__

    >>> mark = User('mwatney', 'Ares3')
    >>> assert mark.firstname == 'mwatney'
    >>> assert mark.lastname == 'Ares3'
    >>> assert mark.groups == ['user']

    >>> melissa = User('mlewis', 'Nasa1', groups=['user', 'staff', 'admin'])
    >>> assert melissa.firstname == 'mlewis'
    >>> assert melissa.lastname == 'Nasa1'
    >>> assert melissa.groups == ['user', 'staff', 'admin']

    >>> assert id(mark.groups) != id(melissa.groups)
"""
from dataclasses import dataclass, field


# Create dataclass `User`, with attributes:
# - `firstname: str` (required)
# - `lastname: str` (required)
# - `groups: list[str]` (optional), default: ['user']
# type: type[User]
@dataclass
class User:
    ...


