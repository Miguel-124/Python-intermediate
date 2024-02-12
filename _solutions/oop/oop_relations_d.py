
def convert(user: User):
    user = vars(user)
    groups = map(vars, user.pop('groups'))
    for i, group in enumerate(groups, start=1):
        for field,value in group.items():
            column_name = f'group{i}_{field}'
            user[column_name] = value
    return user


result = map(convert, DATA)
