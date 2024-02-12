"""
* Assignment: Database Select All
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `users`
       b. columns: all
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `users`
       b. kolumny: wszystkie
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

    >>> pprint(list(data), sort_dicts=False, width=250)
    [{'id': 1, 'firstname': 'Mark', 'lastname': 'Watney', 'group': 'users', 'gender': 'male', 'birthdate': '1994-10-12', 'ssn': '94101212345', 'email': 'mwatney@nasa.gov', 'phone': '+1 (234) 555-0000'},
     {'id': 2, 'firstname': 'Melissa', 'lastname': 'Lewis', 'group': 'admins', 'gender': 'female', 'birthdate': '1995-07-15', 'ssn': '95071512345', 'email': 'mlewis@nasa.gov', 'phone': '+1 (234) 555-0001'},
     {'id': 3, 'firstname': 'Rick', 'lastname': 'Martinez', 'group': 'users', 'gender': 'male', 'birthdate': '1996-01-21', 'ssn': '96012112345', 'email': 'rmartinez@nasa.gov', 'phone': '+1 (234) 555-0010'},
     {'id': 4, 'firstname': 'Alex', 'lastname': 'Vogel', 'group': 'staff', 'gender': 'male', 'birthdate': '1994-11-15', 'ssn': '94111512345', 'email': 'avogel@esa.int', 'phone': '+49 (234) 555-0011'},
     {'id': 5, 'firstname': 'Beth', 'lastname': 'Johanssen', 'group': 'admins', 'gender': 'female', 'birthdate': '2006-05-09', 'ssn': '06250912345', 'email': 'bjohanssen@nasa.gov', 'phone': '+1 (234) 555-0100'},
     {'id': 6, 'firstname': 'Chris', 'lastname': 'Beck', 'group': 'users', 'gender': 'male', 'birthdate': '1999-08-02', 'ssn': '99080212345', 'email': 'cbeck@nasa.gov', 'phone': '+1 (234) 555-0101'}]
"""

# Write SQL query to select data:
# - table: `users`
# - columns: all
# result: str
result = """

-- replace this comment
-- with your sql query

"""

