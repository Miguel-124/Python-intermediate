"""
* Assignment: Database Group By
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `users`
       b. column: `group`
       c. what: unique group names
       d. use: GROUP BY
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `users`
       b. kolumna: `group`
       c. jakie: unikalne nazwy group
       d. użyj: GROUP BY
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

    >>> pprint(list(data), sort_dicts=False, width=20)
    [{'group': 'admins'},
     {'group': 'staff'},
     {'group': 'users'}]
"""

# Write SQL query to select data:
# - table: `users`
# - column: `group`
# - what: unique group names
# - use: GROUP BY
result = """

SELECT `group`
FROM `users`

"""

