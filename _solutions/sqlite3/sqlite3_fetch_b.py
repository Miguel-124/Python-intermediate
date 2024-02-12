
data = []
for line in DATA.splitlines():
    d,t,lvl,msg = line.strip().split(', ', maxsplit=3)
    d = date.fromisoformat(d)
    t = time.fromisoformat(t)
    dt = datetime.combine(d,t)
    data.append((dt, lvl, msg))


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, data)
    result = list(db.execute(SQL_SELECT))
