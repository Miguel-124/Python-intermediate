
result_group = {}
result_shadow = {}
result_passwd = {}
result = []

try:
    with open(FILE_GROUP, encoding='utf-8') as file:
        etc_group = file.readlines()
except FileNotFoundError:
    print(f'File {FILE_GROUP} does not exist')
except PermissionError:
    print('Permission denied')

try:
    with open(FILE_SHADOW, encoding='utf-8') as file:
        etc_shadow = file.readlines()
except FileNotFoundError:
    print(f'File {FILE_SHADOW} does not exist')
except PermissionError:
    print('Permission denied')

try:
    with open(FILE_PASSWD, encoding='utf-8') as file:
        etc_passwd = file.readlines()
except FileNotFoundError:
    print(f'File {FILE_PASSWD} does not exist')
except PermissionError:
    print('Permission denied')

for line in etc_group:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    group_name, _, _, members, *_ = line.split(':')

    if not members:
        continue

    for member in members.split(','):
        if member not in result_group.keys():
            result_group[member] = list()

        result_group[member].append(group_name)

for line in etc_shadow:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    username, password, last_change, *_ = line.split(':')
    timestamp = int(last_change) * DAY
    last_change = date.fromtimestamp(timestamp)

    if password.startswith('$'):
        locked = False
        password = password.split('$')
        password_algorithm = ALGORITHMS[password[1]]
        password_salt = password[2]
        password_password = password[3]
    else:
        locked = True
        password_algorithm = None
        password_salt = None
        password_password = None

    result_shadow[username] = {
        'password': password_password,
        'salt': password_salt,
        'algorithm': password_algorithm,
        'last_change': last_change,
        'locked': locked,
    }

for line in etc_passwd:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    record = line.split(':')
    username = record[0]

    result_passwd[username] = {
        'password': record[1],
        'uid': int(record[2]),
        'gid': int(record[3]),
        'gecos': record[4],
        'home': record[5],
        'shell': record[6],
    }

for user in result_passwd:
    passwd = result_passwd.get(user)
    groups = result_group.get(user)
    shadow = result_shadow.get(user)

    if passwd['uid'] >= 1000:
        continue

    result.append({
        'username': user,
        'uid': passwd['uid'],
        'gid': passwd['gid'],
        'home': passwd['home'],
        'shell': passwd['shell'],
        'algorithm': shadow['algorithm'],
        'password': shadow['password'],
        'groups': groups,
        'last_changed': shadow['last_change'],
        'locked': shadow['locked']})
