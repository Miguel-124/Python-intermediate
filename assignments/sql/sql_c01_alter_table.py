"""
* Assignment: Database Alter Table
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to add column:
       a. table: `contacts`
       b. column: `group`
       c. type: text
       d. default: guest
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby dodać kolumnę:
       a. tabela: `contacts`
       b. kolumna: `group`
       c. type: text
       d. wartość domyślna: guest
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
    ...    assert 'duplicate column name: group' in str(e)

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
    >>> assert ('contacts', 'group', 'TEXT', 0, 'guest', 0) in pragma

    >>> db.close()
"""

# Write SQL query to add column:
# - table: `contacts`
# - column: `group`
# - type: text
# - default: guest
# type: str
result = """

-- replace this comment
-- with your sql query

"""

