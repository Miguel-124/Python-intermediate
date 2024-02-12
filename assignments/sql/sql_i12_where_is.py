"""
* Assignment: Database Where Is
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `users`
       b. columns: `firstname`, `lastname`
       c. where: `lastname` is unknown
       d. use: IS
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `users`
       b. kolumny: `firstname`, `lastname`
       c. gdzie: `lastname` jest nieznana
       d. użyj: IS
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
    []
"""

# Write SQL query to select data:
# - table: `users`
# - columns: `firstname`, `lastname`
# - where: `lastname` is unknown
# - use: IS
# type: str
result = """

SELECT `firstname`, `lastname`
FROM `users`
WHERE `lastname`

"""

