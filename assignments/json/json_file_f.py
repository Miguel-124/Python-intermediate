"""
* Assignment: JSON File Load
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Read data from `FILE`
    2. Convert data to `result: list[tuple]`
    3. Add header as a first line
    4. Run doctests - all must succeed

Polish:
    1. Odczytaj dane z pliku `FILE`
    2. Przekonwertuj dane do `result: list[tuple]`
    3. Doda nagłówek jako pierwszą linia
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert len(result) > 0, \
    'Variable `result` should not be empty'
    >>> assert all(type(row) is tuple for row in result), \
    'Variable `result` should be a list[tuple]'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('petal_length', 'petal_width', 'sepal_length', 'sepal_width', 'species'), (None, None, 5.1, 3.5, 'setosa'), (4.1, 1.3, None, None, 'versicolor'), (None, 1.8, 6.3, None, 'virginica'), (None, 0.2, 5.0, None, 'setosa'), (4.1, None, None, 2.8, 'versicolor'), (None, 1.8, None, 2.9, 'virginica')]

"""

import json


FILE = r'_temporary.json'

DATA = """[
{"sepal_length": 5.1, "sepal_width": 3.5, "species": "setosa"},
{"petal_length": 4.1, "petal_width": 1.3, "species": "versicolor"},
{"sepal_length": 6.3, "petal_width": 1.8, "species": "virginica"},
{"sepal_length": 5.0, "petal_width": 0.2, "species": "setosa"},
{"sepal_width": 2.8, "petal_length": 4.1, "species": "versicolor"},
{"sepal_width": 2.9, "petal_width": 1.8, "species": "virginica"}
]"""

with open(FILE, mode='w') as file:
    file.write(DATA)

# type: list[tuple]
with open(FILE, mode='r') as file:
    data = json.load(file)

result = []

header = tuple(data[0].keys())
result.append(header)

rows = [tuple(row.values()) for row in data]
result.extend(rows)

