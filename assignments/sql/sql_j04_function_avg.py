"""
* Assignment: Database Function Avg
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `products`
       b. columns: `price`
       c. what: average price of all products
       d. use: AVG()
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `products`
       b. kolumny: `price`
       c. co: średnią cenę wszystkich produktów
       d. użyj: AVG()
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
    [{'AVG(`price`)': 440.1456}]
"""

# Write SQL query to select data:
# - table: `products`
# - columns: price
# - what: average price of all products
# - use: AVG()
result = """

SELECT `price`
FROM `products`

"""

