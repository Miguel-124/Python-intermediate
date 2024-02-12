"""
* Assignment: Database Connection Test
* Complexity: easy
* Lines of code: 0 lines
* Time: 2 min

English:
    1. Run file to download and check database file
    2. Run doctests - all must succeed

Polish:
    1. Uruchom plik aby ściągnąć i sprawdzić plik bazy danych
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> import sqlite3

    >>> assert database.exists(), \
    'Error downloading database file'

    >>> assert database.stat().st_size > 0, \
    'Database did not download properly'

    >>> db = sqlite3.connect(database)

    >>> TABLES = 'SELECT `name` FROM `sqlite_master` WHERE `type`="table"'
    >>> tables = {row[0] for row in db.execute(TABLES)}
    >>> assert 'users' in tables
    >>> assert 'products' in tables
    >>> assert 'orders' in tables
    >>> assert 'addresses' in tables

    >>> INDEXES = 'SELECT `name` FROM `sqlite_master` WHERE `type`="index"'
    >>> indexes = {row[0] for row in db.execute(INDEXES)}
    >>> assert 'users_lastname_firstname' in indexes
    >>> assert 'products_ean13' in indexes
    >>> assert 'products_name' in indexes
    >>> assert 'orders_user' in indexes
    >>> assert 'addresses_country' in indexes

    >>> USERS = 'SELECT COUNT(*) FROM `users`'
    >>> users_count = db.execute(USERS).fetchone()[0]
    >>> assert users_count == 6

    >>> PRODUCTS = 'SELECT COUNT(*) FROM `products`'
    >>> products_count = db.execute(PRODUCTS).fetchone()[0]
    >>> assert products_count == 25

    >>> ORDERS = 'SELECT COUNT(*) FROM `orders`'
    >>> orders_count = db.execute(ORDERS).fetchone()[0]
    >>> assert orders_count == 33

    >>> ADDRESSES = 'SELECT COUNT(*) FROM `addresses`'
    >>> addresses_count = db.execute(ADDRESSES).fetchone()[0]
    >>> assert addresses_count == 8

    >>> db.close()
"""

from urllib.request import urlopen
from pathlib import Path


DATA = 'https://python3.info/_static/shop.db'
database = Path(__file__).parent / 'shop.db'

with urlopen(DATA) as db:
    content = db.read()
    database.write_bytes(content)


