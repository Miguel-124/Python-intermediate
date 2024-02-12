"""
* Assignment: OOP Property Age
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define class `User` with attributes:
        a. Attribute `firstname: str`
        b. Attribute `lastname: str`
        c. Attribute `birthdate: date`
        d. Property `age`
    2. Accessing `age` should return user's age in full years
    3. Run doctests - all must succeed

Polish:
    1. Define class `User` with attributes:
        a. Atrybut `firstname: str`
        b. Atrybut `lastname: str`
        c. Atrybut `birthdate: date`
        d. Property `age`
    2. Dostęp do `age` powinien zwrócić wiek użytkownika w pełnych latach
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * date.today()
    * timedelta.days
    * int()

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mark = User(
    ...     firstname='Mark',
    ...     lastname='Watney',
    ...     birthdate=date(2000, 1, 1))

    >>> assert hasattr(mark, 'age'), \
    'Define property `age`'

    >>> mark.age
    24
"""

from dataclasses import dataclass
from datetime import date

YEAR = 365.25


@dataclass
class User:
    firstname: str
    lastname: str
    birthdate: date

    # Accessing `age` should return user's age in full years
    # type: Callable[[Self], int]
    @property
    def age(self):
        return int((date.today() - self.birthdate).days/YEAR)


