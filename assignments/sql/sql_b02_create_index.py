"""
* Assignment: Database Create Index
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to create index:
       a. name: `contacts_lastname`
       b. table: `contacts`
       c. column: `lastname`
       d. use: IF NOT EXISTS
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby stworzyć indeks:
       a. nazwa: `contacts_lastname`
       b. tabela: `contacts`
       c. kolumna: `lastname`
       d. użyj: IF NOT EXISTS
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
    ...     assert 'index contacts_lastname already exists' in str(e)

    >>> INDEXES = 'SELECT `name` FROM `sqlite_master` WHERE `type`="index"'
    >>> indexes = {row[0] for row in db.execute(INDEXES)}
    >>> assert 'contacts_lastname' in indexes

    >>> PRAGMA = '''
    ...     SELECT
    ...         `m`.`tbl_name` AS `table_name`,
    ...         `il`.`name` AS `index_name`,
    ...         `ii`.`name` AS `column_name`,
    ...         CASE `il`.`origin` WHEN 'pk' THEN 1 ELSE 0 END AS `is_primary_key`,
    ...         CASE `il`.[unique] WHEN 1 THEN 0 ELSE 1 END AS `non_unique`,
    ...         `il`.[unique] AS `is_unique`,
    ...         `il`.`partial`,
    ...         `il`.`seq` AS `sequence_in_index`
    ...     FROM `sqlite_master` AS `m`,
    ...         `pragma_index_list`(`m`.`name`) AS `il`,
    ...         `pragma_index_info`(`il`.`name`) AS `ii`
    ...     WHERE `m`.`type` = 'table'
    ...       AND `m`.`tbl_name` = 'contacts'
    ...     GROUP BY
    ...         `m`.`tbl_name`,
    ...         `il`.`name`,
    ...         `ii`.`name`,
    ...         `il`.`origin`,
    ...         `il`.`partial`,
    ...         `il`.`seq`
    ...     ORDER BY 1, 6
    ... '''

    >>> pragma = db.execute(PRAGMA).fetchall()
    >>> assert ('contacts', 'contacts_lastname', 'lastname', 0, 1, 0, 0, 0) in pragma

    >>> db.close()
"""

# Write SQL query to create index:
# - name: `contacts_lastname`
# - table: `contacts`
# - column: `lastname`
# - use: IF NOT EXISTS
# type: str
result = """

-- replace this comment
-- with your sql query

"""

