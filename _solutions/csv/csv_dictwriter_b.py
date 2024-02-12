
fieldnames = set()
for row in DATA:
    fieldnames.update(row.keys())

with open(FILE, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(f=file,
                            fieldnames=sorted(fieldnames),
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL,
                            lineterminator='\n')
    writer.writeheader()
    writer.writerows(DATA)
