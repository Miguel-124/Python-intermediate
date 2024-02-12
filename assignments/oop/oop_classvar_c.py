"""
* Assignment: OOP AttributeClassVar Dataclass
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define class User with class variables:
        a. firstname: str (no default value)
        b. lastname: str (no default value)
    2. Use `dataclass`
    3. Use `typing`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę User z polami klasowymi:
        a. firstname: str (bez domyślnej wartości)
        b. lastname: str (bez domyślnej wartości)
    2. Użyj `dataclass`
    3. Użyj `typing`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from dataclasses import _FIELD_CLASSVAR

    >>> assert isclass(User)
    >>> assert hasattr(User, '__annotations__')
    >>> assert hasattr(User, '__dataclass_fields__')

    >>> fields = User.__dataclass_fields__
    >>> assert 'firstname' in fields
    >>> assert 'lastname' in fields
    >>> assert fields['firstname']._field_type is _FIELD_CLASSVAR
    >>> assert fields['lastname']._field_type is _FIELD_CLASSVAR
"""
from dataclasses import dataclass
from typing import ClassVar


# Define class User with class variables:
# - firstname: str (no default value)
# - lastname: str (no default value)
# Use `dataclass` and `typing`
# type: type[User]
@dataclass
class User:
    firstname: ClassVar[str]
    lastname: ClassVar[str] = None


