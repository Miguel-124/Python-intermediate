"""
* Assignment: Database Insert Tuple
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to insert data:
       a. table: `contacts`
       b. data: `DATA: tuple`
       c. use: prepared statement (with `?`)
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wstawić dane:
       a. tabela: `contacts`
       b. dane: `DATA: tuple`
       c. użyj: przygotowanego zapytania (z `?`)
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'shop.db'
    >>> db = sqlite3.connect(database)
    >>> _ = db.execute(result, DATA)
    >>> db.commit()

    >>> USERS = 'SELECT COUNT(*) FROM `contacts`'
    >>> users_count = db.execute(USERS).fetchone()[0]
    >>> assert users_count >= 2

    >>> db.close()
"""

DATA = ('Melissa', 'Lewis')

# Write SQL query to insert data:
# - table: `contacts`
# - data: `DATA: tuple`
# - use: prepared statement (with `?`)
# type: str
result = """

INSERT INTO `contacts` (`firstname`, `lastname`)
VALUES ()

"""

