"""
* Assignment: Database Select OrderByNulls
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `users`
       b. columns: `firstname`, `lastname`
       c. order1: `lastname `ascending empty values last
       d. order2: `firstname descending empty values first
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `users`
       b. kolumny: `firstname`, `lastname`
       c. kolejność1: `lastname` rosnąco wartości puste na końcu
       d. kolejność2: `firstname` malejąco wartości puste na początku
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
    [{'firstname': 'Chris', 'lastname': 'Beck'},
     {'firstname': 'Beth', 'lastname': 'Johanssen'},
     {'firstname': 'Melissa', 'lastname': 'Lewis'},
     {'firstname': 'Rick', 'lastname': 'Martinez'},
     {'firstname': 'Alex', 'lastname': 'Vogel'},
     {'firstname': 'Mark', 'lastname': 'Watney'}]
"""

# Write SQL query to select data:
# - table: `users`
# - columns: `firstname`, `lastname`
# - order1: `lastname` descending empty values last
# - order2: `firstname` ascending empty values first
# type: str
result = """

SELECT `firstname`, `lastname`
FROM `users`
ORDER BY
    `lastname` ASC,
    `firstname` DESC

"""

