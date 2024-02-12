"""
* Assignment: Database Select Alias
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `users`
       b. columns: `firstname`, `lastname`
       c. alias: `firstname` as `fname`
       d. alias: `lastname` as `lname`
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `users`
       b. kolumny: `firstname`, `lastname`
       c. alias: `firstname` jako `fname`
       d. alias: `lastname` jako `lname`
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
    [{'fname': 'Chris', 'lname': 'Beck'},
     {'fname': 'Beth', 'lname': 'Johanssen'},
     {'fname': 'Melissa', 'lname': 'Lewis'},
     {'fname': 'Rick', 'lname': 'Martinez'},
     {'fname': 'Alex', 'lname': 'Vogel'},
     {'fname': 'Mark', 'lname': 'Watney'}]
"""

# Write SQL query to select data:
# - table: `users`
# - columns: `firstname`, `lastname`
# - alias: `firstname` as `fname`
# - alias: `lastname` as `lname`
# result: str
result = """

SELECT `firstname`, `lastname`
FROM `users`

"""

