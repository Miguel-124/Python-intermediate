"""
* Assignment: Database Update All
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to update all records:
       a. table: `contacts`
       b. where: all
       c. column: `group`
       d. value: 'users'
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby zaktualizować wszystkie rekordy:
       a. tabela: `contacts`
       b. gdzie: wszystkie
       c. kolumna: `group`
       d. wartość: 'users'
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'shop.db'
    >>> db = sqlite3.connect(database)
    >>> _ = db.execute(result)
    >>> db.commit()

    >>> USERS = 'SELECT COUNT(*) FROM `contacts` WHERE `group` == "users"'
    >>> users = db.execute(USERS).fetchone()[0]
    >>> assert users >= 9

    >>> db.close()
"""

# Write SQL query to update all records:
# - table: `contacts`
# - where: all
# - column: `group`
# - value: 'users'
# type: str
result = """

-- replace this comment
-- with your sql query

"""

