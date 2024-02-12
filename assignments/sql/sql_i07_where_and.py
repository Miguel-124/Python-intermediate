"""
* Assignment: Database Where And
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `users`
       b. columns: `firstname`, `lastname`, `birthdate`
       c. where: `birthdate` is between '1990-01-01' and '2000-01-01' (inclusive)
       d. use: AND
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `users`
       b. kolumny: `firstname`, `lastname`, `birthdate`
       c. gdzie: `birthdate` jest od '1990-01-01' do '2000-01-01' (włącznie)
       d. użyj: AND
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
    [{'firstname': 'Mark', 'lastname': 'Watney', 'birthdate': '1994-10-12'},
     {'firstname': 'Melissa', 'lastname': 'Lewis', 'birthdate': '1995-07-15'},
     {'firstname': 'Rick', 'lastname': 'Martinez', 'birthdate': '1996-01-21'},
     {'firstname': 'Alex', 'lastname': 'Vogel', 'birthdate': '1994-11-15'},
     {'firstname': 'Chris', 'lastname': 'Beck', 'birthdate': '1999-08-02'}]
"""

# Write SQL query to select data:
# - table: `users`
# - columns: `firstname`, `lastname`, `birthdate`
# - where: `birthdate` is from '1990-01-01' to '2000-01-01' (inclusive)
# - use: AND
# type: str
result = """

SELECT `firstname`, `lastname`, `birthdate`
FROM `users`
WHERE `birthdate`

"""

