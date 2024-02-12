
result = []

for user in DATA:
    user = vars(user)
    groups = [','.join(str(x) for x in vars(group).values())
              for group in user.pop('groups')]
    user['groups'] = ';'.join(groups)
    result.append(user)


fieldnames = sorted(result[0].keys())

with open(FILE, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(result)
