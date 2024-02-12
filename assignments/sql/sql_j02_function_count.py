"""
* Assignment: Database Function Count
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `products`
       b. columns: all
       c. what: count number of rows
       d. use: `COUNT()`
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `products`
       b. kolumny: all
       c. co: zlicz liczbę wierszy
       d. użyj: `COUNT()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'shop.db'
    >>> with sqlite3.connect(database) as db:
    ...    db.row_factory = sqlite3.Row
    ...    data = map(dict, db.execute(result).fetchall())

    >>> pprint(list(data), sort_dicts=False, width=79)
    [{'COUNT(*)': 25}]
"""

# Write SQL query to select data:
# - table: `products`
# - columns: all
# - what: count number of rows
# - use: `COUNT()`
result = """

SELECT *
FROM `products`

"""

