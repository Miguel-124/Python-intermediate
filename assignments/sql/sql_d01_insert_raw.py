"""
* Assignment: Database Insert Raw
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to insert data:
       a. table: `contacts`
       b. firstname: 'Mark'
       c. lastname: 'Watney'
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wstawić dane:
       a. tabela: `contacts`
       b. firstname: 'Mark'
       c. lastname: 'Watney'
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'shop.db'
    >>> db = sqlite3.connect(database)
    >>> _ = db.execute(result)
    >>> db.commit()

    >>> USERS = 'SELECT COUNT(*) FROM `contacts`'
    >>> users_count = db.execute(USERS).fetchone()[0]
    >>> assert users_count >= 1

    >>> db.close()
"""

# Write SQL query to insert data:
# - table: `contacts`
# - firstname: 'Mark'
# - lastname: 'Watney'
# type: str
result = """

-- replace this comment
-- with your sql query

"""

