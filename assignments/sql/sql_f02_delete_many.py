"""
* Assignment: Database Delete Many
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to delete many records:
       a. table: `contacts`
       b. where: `lastname` == 'Watney'
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby skasować wiele rekordów:
       a. tabela: `contacts`
       b. gdzie: `lastname` == 'Watney'
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'shop.db'
    >>> db = sqlite3.connect(database)
    >>> _ = db.execute(result)
    >>> db.commit()

    >>> USERS = 'SELECT COUNT(*) FROM `contacts` WHERE `lastname` == "Watney"'
    >>> users = db.execute(USERS).fetchone()[0]
    >>> assert users == 0

    >>> db.close()
"""

# Write SQL query to delete many records:
# - table: `contacts`
# - where: `lastname` == 'Watney'
# type: str
result = """

-- replace this comment
-- with your sql query

"""

