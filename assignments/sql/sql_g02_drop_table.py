"""
* Assignment: Database Drop Table
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to delete:
       a. table: `contacts`
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby skasować:
       a. tabela: `contacts`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'shop.db'
    >>> db = sqlite3.connect(database)

    >>> try:
    ...     _ = db.execute(result)
    ... except sqlite3.OperationalError as e:
    ...     assert 'no such table: contacts' in str(e)

    >>> INDEXES = 'SELECT `name` FROM `sqlite_master` WHERE `type`="index"'
    >>> indexes = {row[0] for row in db.execute(INDEXES)}
    >>> assert 'contacts_lastname' not in indexes

    >>> db.close()
"""

# Write SQL query to delete:
# - table: `contacts`
# type: str
result = """

-- replace this comment
-- with your sql query

"""

