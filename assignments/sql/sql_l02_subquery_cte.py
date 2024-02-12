"""
* Assignment: Database Subquery CTE
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `users`
       b. columns: `firstname`, `lastname`
       c. where: has 2 or more members
       d. use: CTE - Common Table Expression
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `users`
       b. kolumny: `firstname`, `lastname`
       c. gdzie: mająca 2 lub więcej członków
       d. użyj: CTE - Common Table Expression
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
    [{'firstname': 'Mark', 'lastname': 'Watney'},
     {'firstname': 'Melissa', 'lastname': 'Lewis'},
     {'firstname': 'Rick', 'lastname': 'Martinez'},
     {'firstname': 'Beth', 'lastname': 'Johanssen'},
     {'firstname': 'Chris', 'lastname': 'Beck'}]
"""

# Write SQL query to select data:
# - table: `users`
# - columns: `firstname`, `lastname`
# - where: has 2 or more members
# - use: CTE - Common Table Expression
# type: str
result = """

SELECT `firstname`, `lastname`
FROM `users`
WHERE `group` IN (
    SELECT `group`
    FROM `users`
    GROUP BY `group`
    HAVING COUNT(`group`) >= 2
)

"""

