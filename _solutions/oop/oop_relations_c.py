
def convert(user: dict):
    for i, group in enumerate(user.pop('groups'), start=1):
        for field,value in group.items():
            column_name = f'group{i}_{field}'
            user[column_name] = value
    return user


result = map(convert, DATA)
