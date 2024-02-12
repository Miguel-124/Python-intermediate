
result = []

for user in DATA:
    for i, group in enumerate(user.pop('groups'), start=1):
        for field,value in group.items():
            column_name = f'group{i}_{field}'
            user[column_name] = value
    result.append(user)

fieldnames = set()
for row in result:
    fieldnames.update(row.keys())

with open(FILE, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(fieldnames), quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(result)
