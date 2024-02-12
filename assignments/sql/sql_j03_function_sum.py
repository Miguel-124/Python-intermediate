"""
* Assignment: Database Function Sum
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `products`
       b. columns: `price`
       c. what: sum of prices of all products
       d. use: `SUM()`
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `products`
       b. kolumny: `price`
       c. co: suma cen wszystkich produktów
       d. użyj: `SUM()`
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
    [{'SUM(`price`)': 11003.64}]
"""

# Write SQL query to select data:
# - table: `products`
# - columns: `price`
# - what: sum of prices of all products
# - use: SUM()
result = """

SELECT `price`
FROM `products`

"""

