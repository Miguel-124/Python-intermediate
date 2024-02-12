
result = []

with sqlite3.connect(DATABASE) as connection:
    db = connection.cursor()
    db.row_factory = sqlite3.Row
    db.execute(SQL_CREATE_TABLE_ADDRESSES)
    db.execute(SQL_CREATE_TABLE_ASTRONAUTS)
    db.execute(SQL_CREATE_INDEX_ASTRONAUT_LASTNAME)

    for astronaut in DATA:
        addresses = astronaut.pop('addresses')
        db.execute(SQL_INSERT_ASTRONAUT, astronaut)
        astronaut_id = db.lastrowid
        for address in addresses:
            address['astronaut_id'] = astronaut_id
            db.execute(SQL_INSERT_ADDRESS, address)

    result = [dict(x) for x in db.execute(SQL_SELECT)]
