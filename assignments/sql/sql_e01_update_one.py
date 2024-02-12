"""
* Assignment: Database Update One
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to update one record:
       a. table: `contacts`
       b. where: `id` == 2
       c. column: `group`
       d. value: 'admin'
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby zaktualizować jeden rekord:
       a. tabela: `contacts`
       b. gdzie: `id` == 2
       c. kolumna: `group`
       d. wartość: 'admin'
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'shop.db'
    >>> db = sqlite3.connect(database)
    >>> _ = db.execute(result)
    >>> db.commit()

    >>> USERS = 'SELECT COUNT(*) FROM `contacts` WHERE `group` == "admin"'
    >>> users = db.execute(USERS).fetchone()[0]
    >>> assert users >= 1

    >>> db.close()
"""

# Write SQL query to update one record:
# - table: `contacts`
# - where: `id` == 2
# - column: `group`
# - value: 'admin'
# type: str
result = """

-- replace this comment
-- with your sql query

"""

