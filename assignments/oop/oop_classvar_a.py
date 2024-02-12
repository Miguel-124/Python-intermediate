"""
* Assignment: OOP AttributeClassVar Class
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define class User with class variables:
        a. firstname: str (default 'Mark')
        b. lastname: str (default 'Watney')
    2. Do not use `dataclass`
    3. Do not use `typing`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę User z polami klasowymi:
        a. firstname: str (domyślnie 'Mark')
        b. lastname: str (domyślnie 'Watney')
    2. Nie używaj `dataclass`
    3. Nie używaj `typing`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert hasattr(User, '__annotations__')

    >>> fields = User.__dict__
    >>> assert 'firstname' in fields
    >>> assert 'lastname' in fields
"""


# Define class User with class variables:
# - firstname: str (default 'Mark')
# - lastname: str (default 'Watney')
# Do not use `dataclass`
# Do not use `typing`
# type: type[User]
class User:
    firstname: str = 'Mark'
    lastname = 'Watney'


