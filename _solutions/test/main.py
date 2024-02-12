from datetime import date
from hashlib import sha512

YEAR = 365.25


def encrypt(password: str, salt: str) -> str:
    """
    >>> encrypt('Ares3', 'NASA')
    'f1dd85f79a26d1b8f574359870386b522ad9499e4af969b287bd3b259993171bde4712d638c55cb94330a959c75bc3c4a3d2e338dd6b39b4ce3e80e0924caae0'
    """
    to_encrypt = password + salt
    return sha512(to_encrypt.encode()).hexdigest()


class User:
    lastname: str
    firstname: str
    birthdate: date

    def __init__(self, firstname: str, lastname: str, /, *,
                 birthdate: str | None = None,
                 username: str | None = None,
                 password: str | None = None,
                 ) -> None:
        if username is None and password is not None:
            raise TypeError('Username is required')
        if username is not None and password is None:
            raise TypeError('Password is required')
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = date.fromisoformat(birthdate) if birthdate else None
        self.username = username
        self.password = encrypt(password, username) if password else None  # noqa

    def get_age(self):
        days = (date.today() - self.birthdate).days
        return int(days / YEAR)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def __repr__(self):
        clsname = self.__class__.__name__
        firstname = self.firstname
        lastname = self.lastname
        if self.password is None:
            return f"{clsname}('{firstname}', '{lastname}')"
        else:
            password = '*****'
            return f"{clsname}('{firstname}', '{lastname}', {password=})"
