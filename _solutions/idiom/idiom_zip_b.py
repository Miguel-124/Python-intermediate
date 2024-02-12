
header, *rows = DATA
result = [dict(zip(header, row)) for row in rows]
