"""
* Assignment: Database Function Max
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `products`
       b. column: `name`, `price`
       c. what: the most expensive product
       d. use: MAX()
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `products`
       b. kolumna: `name`, `price`
       c. co: majdroższy produkt
       d. użyj: MAX()
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
    [{'name': 'Romeo', 'MAX(`price`)': 1337.0}]
"""

# Write SQL query to select data:
# - table: `products`
# - column: `name`, `price`
# - what: the most expensive product
# - use: MAX()
result = """

SELECT `name`, `price`
FROM `products`

"""

