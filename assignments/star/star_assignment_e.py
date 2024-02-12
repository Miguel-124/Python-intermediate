"""
* Assignment: Star Assignment Loop
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define `result: set[str]`
    2. Iterating over `DATA` unpack row to:
        a. `values` - all beside last
        b. `species` - last in the row
    3. Append to `result` species names with suffix in `SUFFIXES`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: set[str]`
    2. Iterując po `DATA` rozpakuj wiersz do:
        a. `values` - wszystkie poza ostatnim
        b. `species` - ostatni w wierszu
    3. Dodaj do `result` nazwy gatunków (species) z końcówką w `SUFFIXES`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.endswith()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is set, \
    'Result must be a set'
    >>> assert len(result) > 0, \
    'Result cannot be empty'
    >>> assert all(type(element) is str for element in result), \
    'All elements in result must be a str'

    >>> 'virginica' in result
    True
    >>> 'setosa' in result
    True
    >>> 'versicolor' in result
    False
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

SUFFIXES = ('ca', 'osa')

# species names with suffix in `SUFFIXES`
# type: set[str]
result = set()

for *values, species in DATA[1:]:
    if species.endswith(SUFFIXES):
        result.add(species)

