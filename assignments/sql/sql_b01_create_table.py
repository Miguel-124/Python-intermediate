"""
* Assignment: Database Create Table
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Write SQL query to create table:
       a. table: `contacts`
       b. column: `id`, integer, primary key, autoincrement
       c. column: `firstname`, text
       d. column: `lastname`, text
       e. column: `birthdate`, date, default null
       f. use: IF NOT EXISTS
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby stworzyć tabelę:
       a. tabela: `contacts`
       b. kolumna: `id`, integer, primary key, autoincrement
       c. kolumna: `firstname`, text
       d. kolumna: `lastname`, text
       e. kolumna: `birthdate`, date, default null
       f. użyj: IF NOT EXISTS
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'shop.db'
    >>> db = sqlite3.connect(database)

    >>> try:
    ...     _ = db.execute(result)
    ...     db.commit()
    ... except sqlite3.OperationalError as e:
    ...     assert 'table contacts already exists' in str(e)

    >>> TABLES = 'SELECT `name` FROM `sqlite_master` WHERE `type`="table"'
    >>> tables = {row[0] for row in db.execute(TABLES)}
    >>> assert 'contacts' in tables, \
    'You need to create table named `contacts`'

    >>> PRAGMA = '''
    ...     SELECT
    ...         `m`.`name` AS `table_name`,
    ...         `p`.`name` AS `col_name`,
    ...         `p`.`type` AS `col_type`,
    ...         `p`.`pk` AS `col_is_pk`,
    ...         `p`.`dflt_value` AS `col_default_val`,
    ...         `p`.[notnull] AS `col_is_not_null`
    ...     FROM `sqlite_master` AS `m`
    ...     LEFT OUTER JOIN `pragma_table_info`((`m`.`name`)) AS `p`
    ...                  ON `m`.`name` != `p`.`name`
    ...     WHERE `m`.`type` = 'table'
    ...     ORDER BY `table_name`
    ... '''

    >>> pragma = db.execute(PRAGMA).fetchall()
    >>> assert ('contacts', 'id', 'INTEGER', 1, None, 0) in pragma
    >>> assert ('contacts', 'firstname', 'TEXT', 0, None, 0) in pragma
    >>> assert ('contacts', 'lastname', 'TEXT', 0, None, 0) in pragma
    >>> assert ('contacts', 'birthdate', 'DATE', 0, 'NULL', 0) in pragma

    >>> db.close()
"""

# SQL query to create table:
# - table: `contacts`
# - column: `id`, integer, primary key, autoincrement
# - column: `firstname`, text
# - column: `lastname`, text
# - column: `birthdate`, date, default null
# - use: IF NOT EXISTS
# type: str
result = """

-- replace this comment
-- with your sql query

"""

