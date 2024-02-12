
with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, DATA)
    result = list(db.execute(SQL_SELECT))
