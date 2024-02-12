"""
* Assignment: File Read Passwd
* Type: homework
* Complexity: hard
* Lines of code: 100 lines
* Time: 55 min

English:
    1. Save listings content to files:
        a. `etc_passwd.txt`
        b. `etc_shadow.txt`
        c. `etc_group.txt`
    2. Copy also comments and empty lines
    3. Parse files and convert it to `result: list[dict]`
    4. Return list of users with `UID` greater than 1000
    5. User dict should contains data collected from all files
    6. Run doctests - all must succeed

Polish:
    1. Zapisz treści listingów do plików:
        a. `etc_passwd.txt`
        b. `etc_shadow.txt`
        c. `etc_group.txt`
    2. Skopiuj również komentarze i puste linie
    3. Sparsuj plik i przedstaw go w formacie `result: list[dict]`
    4. Zwróć listę użytkowników, których `UID` jest większy niż 1000
    5. Dict użytkownika powinien zawierać dane z wszystkich plików
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `from datetime import date`
    * `date.fromtimestamp(timestamp: int)`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> pprint(result)
    [{'algorithm': None,
      'gid': 1000,
      'groups': ['user', 'staff'],
      'home': '/home/mwatney',
      'last_changed': datetime.date(2015, 4, 25),
      'locked': True,
      'password': None,
      'shell': '/bin/bash',
      'uid': 1000,
      'username': 'mwatney'},
     {'algorithm': 'SHA-512',
      'gid': 1001,
      'groups': ['user', 'staff', 'admin'],
      'home': '/home/mlewis',
      'last_changed': datetime.date(2015, 7, 16),
      'locked': False,
      'password': 'tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50',
      'shell': '/bin/bash',
      'uid': 1001,
      'username': 'mlewis'},
     {'algorithm': 'MD5',
      'gid': 1002,
      'groups': ['user', 'staff'],
      'home': '/home/rmartinez',
      'last_changed': datetime.date(2005, 2, 11),
      'locked': False,
      'password': 'SWlkjRWexrXYgc98F.',
      'shell': '/bin/bash',
      'uid': 1002,
      'username': 'rmartinez'}]

      >>> from os import remove
      >>> remove(FILE_GROUP)
      >>> remove(FILE_SHADOW)
      >>> remove(FILE_PASSWD)
"""

from datetime import date
from os.path import dirname, join
from pathlib import Path
from typing import NamedTuple

BASE_DIR = dirname(__file__)
FILE_GROUP = join(BASE_DIR, 'etc-group.txt')
FILE_SHADOW = join(BASE_DIR, 'etc-shadow.txt')
FILE_PASSWD = join(BASE_DIR, 'etc-passwd.txt')


CONTENT_GROUP = """##
# `/etc/group` structure
#   - Group Name: from `/etc/passwd`
#   - Group Password: `x` indicates that shadow passwords are used)
#   - GID: Group ID
#   - Members: usernames from `/etc/passwd`
##

root::0:root
other::1:
bin::2:root,bin,daemon
sys::3:root,bin,sys,adm
adm::4:root,adm,daemon
mail::6:root
daemon::12:root,daemon
sysadmin::14:root
user::1001:mwatney,mlewis,rmartinez
staff::1002:mwatney,mlewis,rmartinez
admin::1003:mlewis
nobody::60001:
noaccess::60002:
nogroup::65534:"""


CONTENT_PASSWD = """##
# `/etc/passwd` structure:
#   - Username
#   - Password: `x` indicates that shadow passwords are used
#   - UID: User ID number
#   - GID: User's group ID number
#   - GECOS: Full name of the user
#   - Home directory
#   - Login shell
##

root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
mwatney:x:1000:1000:Mark mwatney:/home/mwatney:/bin/bash
mlewis:x:1001:1001:Melissa mlewis:/home/mlewis:/bin/bash
rmartinez:x:1002:1002:Rick rmartinez:/home/rmartinez:/bin/bash"""


CONTENT_SHADOW = """##
# `/etc/shadow` structure
#   - Username: from `/etc/passwd`
#   - Password
#   - Last Password Change: Days since 1970-01-01
#   - Minimum days between password changes: 0 - changed at any time
#   - Password validity: Days after which password must be changed, 99999 - many, many years
#   - Warning threshold: Days to warn user of an expiring password, 7 - full week
#   - Account inactive: Days after password expires and account is disabled
#   - Time since account is disabled: Days since 1970-01-01
#   - A reserved field for possible future use
#
# Password field (split by `$`):
#   - algorithm
#   - salt
#   - password hash
#
# Password algorithms:
#   - `1` - MD5
#   - `2a` - Blowfish
#   - `2y` - Blowfish
#   - `5` - SHA-256
#   - `6` - SHA-512
#
# Password special chars:
#   - ` ` (blank entry) - password is not required to log in
#   - `*` (asterisk) - account is disabled, cannot be unlocked, no password has ever been set
#   - `!` (exclamation mark) - account is locked, can be unlocked, no password has ever been set
#   - `!<password_hash>` - account is locked, can be unlocked, but password is set
#   - `!!` (two exclamation marks) - account created, waiting for initial password to be set by admin
##

root:$6$Ke02nYgo.9v0SF4p$hjztYvo/M4buqO4oBX8KZTftjCn6fE4cV5o/I95QPekeQpITwFTRbDUBYBLIUx2mhorQoj9bLN8v.w6btE9xy1:16431:0:99999:7:::
adm:$6$5H0QpwprRiJQR19Y$bXGOh7dIfOWpUb/Tuqr7yQVCqL3UkrJns9.7msfvMg4ZO/PsFC5Tbt32PXAw9qRFEBs1254aLimFeNM8YsYOv.:16431:0:99999:7:::
mwatney:!!:16550::::::
mlewis:$6$P9zn0KwR$tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50:16632:0:99999:7:::
rmartinez:$1$.QKDPc5E$SWlkjRWexrXYgc98F.:12825:0:90:5:30:13096:"""

with open(FILE_GROUP, mode='w') as file:
    file.write(CONTENT_GROUP)

with open(FILE_PASSWD, mode='w') as file:
    file.write(CONTENT_PASSWD)

with open(FILE_SHADOW, mode='w') as file:
    file.write(CONTENT_SHADOW)

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

ALGORITHMS = {
    '1': 'MD5',
    '2a': 'Blowfish',
    '2y': 'Blowfish',
    '5': 'SHA-256',
    '6': 'SHA-512',
}


class Account(NamedTuple):
    username: str
    password: str
    uid: int
    gid: int
    gecos: str | None
    home: str
    shell: str


class Shadow(NamedTuple):
    username: str
    password_hash: str | None
    password_salt: str | None
    password_algorithm: str | None
    last_changed: int | None
    minimum: int | None
    maximum: int | None
    warning: int | None
    inactive: int | None
    disabled: int | None
    locked: bool
    reserved: str | None


class Group(NamedTuple):
    groupname: str
    password: str | None
    gid: int
    members: list[str]


def valid_line(line: str) -> bool:
    """
    >>> valid_line('')
    False
    >>> valid_line('# comment')
    False
    >>> valid_line('root:x:0:0:root:/root:/bin/bash')
    True
    """
    if len(line) == 0:
        return False
    if line.startswith('#'):
        return False
    return True


def parse_passwd(line: str) -> Account:
    """
    root:x:0:0:root:/root:/bin/bash
    bin:x:1:1:bin:/bin:/sbin/nologin
    daemon:x:2:2:daemon:/sbin:/sbin/nologin
    adm:x:3:4:adm:/var/adm:/sbin/nologin
    shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
    halt:x:7:0:halt:/sbin:/sbin/halt
    nobody:x:99:99:Nobody:/:/sbin/nologin
    sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
    mwatney:x:1000:1000:Mark mwatney:/home/mwatney:/bin/bash
    mlewis:x:1001:1001:Melissa mlewis:/home/mlewis:/bin/bash
    rmartinez:x:1002:1002:Rick rmartinez:/home/rmartinez:/bin/bash

    >>> parse_passwd('root:x:0:0:root:/root:/bin/bash')
    Account(username='root', password='x', uid=0, gid=0, gecos='root', home='/root', shell='/bin/bash')

    >>> parse_passwd('bin:x:1:1:bin:/bin:/sbin/nologin')
    Account(username='bin', password='x', uid=1, gid=1, gecos='bin', home='/bin', shell='/sbin/nologin')

    >>> parse_passwd('mwatney:x:1000:1000:Mark mwatney:/home/mwatney:/bin/bash')
    Account(username='mwatney', password='x', uid=1000, gid=1000, gecos='Mark mwatney', home='/home/mwatney', shell='/bin/bash')

    >>> parse_passwd('rmartinez:x:1002:1002:Rick rmartinez:/home/rmartinez:/bin/bash')
    Account(username='rmartinez', password='x', uid=1002, gid=1002, gecos='Rick rmartinez', home='/home/rmartinez', shell='/bin/bash')
    """
    username, password, uid, gid, gecos, home, shell = line.split(':')
    return Account(
        username=username,
        password=password,
        uid=int(uid),
        gid=int(gid),
        gecos=gecos if gecos else None,
        home=home,
        shell=shell,
    )


def parse_group(line: str) -> Group:
    """
    root::0:root
    other::1:
    bin::2:root,bin,daemon
    sys::3:root,bin,sys,adm
    adm::4:root,adm,daemon
    mail::6:root
    daemon::12:root,daemon
    sysadmin::14:root
    user::1001:mwatney,mlewis,rmartinez
    staff::1002:mwatney,mlewis,rmartinez
    admin::1003:mlewis
    nobody::60001:
    noaccess::60002:
    nogroup::65534:

    >>> parse_group('root::0:root')
    Group(groupname='root', password='', gid=0, members=['root'])

    >>> parse_group('user::1001:mwatney,mlewis,rmartinez')
    Group(groupname='user', password='', gid=1001, members=['mwatney', 'mlewis', 'rmartinez'])

    >>> parse_group('staff::1002:mwatney,mlewis,rmartinez')
    Group(groupname='staff', password='', gid=1002, members=['mwatney', 'mlewis', 'rmartinez'])
    """
    groupname, password, gid, members = line.split(':')
    return Group(
        groupname=groupname,
        password=password,
        gid=int(gid),
        members=members.split(',') if members else []
    )


def parse_shadow(line: str) -> Shadow:
    """
    Password algorithms:
      - `1` - MD5
      - `2a` - Blowfish
      - `2y` - Blowfish
      - `5` - SHA-256
      - `6` - SHA-512

    Password special chars:
      - ` ` (blank entry) - password is not required to log in
      - `*` (asterisk) - account is disabled, cannot be unlocked, no password has ever been set
      - `!` (exclamation mark) - account is locked, can be unlocked, no password has ever been set
      - `!<password_hash>` - account is locked, can be unlocked, but password is set
      - `!!` (two exclamation marks) - account created, waiting for initial password to be set by admin

    Example:
        root:$6$Ke02nYgo.9v0SF4p$hjztYvo/M4buqO4oBX8KZTftjCn6fE4cV5o/I95QPekeQpITwFTRbDUBYBLIUx2mhorQoj9bLN8v.w6btE9xy1:16431:0:99999:7:::
        adm:$6$5H0QpwprRiJQR19Y$bXGOh7dIfOWpUb/Tuqr7yQVCqL3UkrJns9.7msfvMg4ZO/PsFC5Tbt32PXAw9qRFEBs1254aLimFeNM8YsYOv.:16431:0:99999:7:::
        mwatney:!!:16550::::::
        mlewis:$6$P9zn0KwR$tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50:16632:0:99999:7:::
        rmartinez:$1$.QKDPc5E$SWlkjRWexrXYgc98F.:12825:0:90:5:30:13096:

    >>> parse_shadow('root:$6$Ke02nYgo.9v0SF4p$hjztYvo/M4buqO4oBX8KZTftjCn6fE4cV5o/I95QPekeQpITwFTRbDUBYBLIUx2mhorQoj9bLN8v.w6btE9xy1:16431:0:99999:7:::')
    Shadow(username='root', password_hash='hjztYvo/M4buqO4oBX8KZTftjCn6fE4cV5o/I95QPekeQpITwFTRbDUBYBLIUx2mhorQoj9bLN8v.w6btE9xy1', password_salt='Ke02nYgo.9v0SF4p', password_algorithm='SHA-512', last_changed=datetime.date(2014, 12, 27), minimum=0, maximum=99999, warning=7, inactive=None, disabled=None, locked=False, reserved=None)

    >>> parse_shadow('mwatney:!!:16550::::::')
    Shadow(username='mwatney', password_hash=None, password_salt=None, password_algorithm=None, last_changed=datetime.date(2015, 4, 25), minimum=None, maximum=None, warning=None, inactive=None, disabled=None, locked=True, reserved=None)

    >>> parse_shadow('rmartinez:$1$.QKDPc5E$SWlkjRWexrXYgc98F.:12825:0:90:5:30:13096:')
    Shadow(username='rmartinez', password_hash='SWlkjRWexrXYgc98F.', password_salt='.QKDPc5E', password_algorithm='MD5', last_changed=datetime.date(2005, 2, 11), minimum=0, maximum=90, warning=5, inactive=30, disabled=13096, locked=False, reserved=None)
    """
    username, password, last_changed, minimum, maximum, warning, inactive, disabled, reserved = line.split(':')
    if password == '!!':
        locked = True
        algorithm = None
        salt = None
        hash = None
    elif password == '!':
        locked = True
        algorithm = None
        salt = None
        hash = None
    elif password == '*':
        locked = True
        algorithm = None
        salt = None
        hash = None
    else:
        locked = False
        _, algorithm, salt, hash = password.split('$')
        algorithm = ALGORITHMS.get(algorithm)
    return Shadow(
        username=username,
        password_hash=hash,
        password_salt=salt,
        password_algorithm=algorithm,
        last_changed=date.fromtimestamp(int(last_changed) * DAY) if last_changed else None,
        minimum=int(minimum) if minimum else None,
        maximum=int(maximum) if maximum else None,
        warning=int(warning) if warning else None,
        inactive=int(inactive) if inactive else None,
        disabled=int(disabled) if disabled else None,
        locked=locked,
        reserved=reserved if reserved else None,
    )


shadows = Path(FILE_SHADOW).read_text().splitlines()
shadows = map(str.strip, shadows)
shadows = filter(valid_line, shadows)
shadows = map(parse_shadow, shadows)
shadows = {shadow.username: shadow for shadow in shadows}


groups = Path(FILE_GROUP).read_text().splitlines()
groups = map(str.strip, groups)
groups = filter(valid_line, groups)
groups = map(parse_group, groups)
user_groups = {}
for group in groups:
    for user in group.members:
        if user not in user_groups:
            user_groups[user] = []
        user_groups[user].append(group.groupname)


users = Path(FILE_PASSWD).read_text().splitlines()
users = map(str.strip, users)
users = filter(valid_line, users)
users = map(parse_passwd, users)


result = []
for user in users:
    passwd = user
    shadow = shadows.get(user.username, None)
    group = user_groups.get(user.username, [])
    if passwd.uid >= 1000:
        result.append({
            'algorithm': shadow.password_algorithm,
            'gid': passwd.gid,
            'groups': group,
            'home': passwd.home,
            'last_changed': shadow.last_changed,
            'locked': shadow.locked,
            'password': shadow.password_hash,
            'shell': passwd.shell,
            'uid': passwd.uid,
            'username': passwd.username})
