from datetime import date
from unittest import TestCase
from unittest.mock import patch
from main import User

ENCRYPTED_PASSWORD = (
    'c57e1907bca9dc04683573c61544cc14cbce240e8e7f'
    'f2ff990972e43d4c837d1fe3c94f867dd21c22188d54'
    '2043769b8e868a8f47a4818811a6918017e2d68a'
)


class UserInitTest(TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            User()  # noqa


class UserNameTest(TestCase):
    def test_name_init_firstname_only(self):
        with self.assertRaises(TypeError):
            User('Mark')  # noqa

    def test_name_init_positional(self):
        mark = User('Mark', 'Watney')
        self.assertIsInstance(mark, User)
        self.assertEqual(mark.firstname, 'Mark')
        self.assertEqual(mark.lastname, 'Watney')

    def test_name_init_keyword(self):
        with self.assertRaises(TypeError):
            User(firstname='Mark', lastname='Watney')  # noqa

    def test_name_str(self):
        mark = User('Mark', 'Watney')
        self.assertEqual(str(mark), 'Mark Watney')

    def test_name_repr(self):
        mark = User('Mark', 'Watney')
        self.assertEqual(repr(mark), "User('Mark', 'Watney')")


class UserBirthdateTest(TestCase):
    def test_birthdate_init_positional(self):
        with self.assertRaises(TypeError):
            User('Mark', 'Watney', '2000-01-02')  # noqa

    def test_birthdate_init_keyword(self):
        mark = User('Mark', 'Watney', birthdate='2000-01-02')
        self.assertIsInstance(mark.birthdate, date)
        self.assertEqual(mark.birthdate, date(2000, 1, 2))

    def test_birthdate_age(self):
        mark = User('Mark', 'Watney', birthdate='2000-01-02')
        with patch('main.date') as d:
            d.today.return_value = date(2024, 1, 2)
            age = mark.get_age()
        self.assertEqual(age, 24)


class UserCredentialsTest(TestCase):
    def test_credentials_init_username(self):
        with self.assertRaises(TypeError):
            mark = User('Mark', 'Watney', username='mwatney')  # noqa

    def test_credentials_init_password(self):
        with self.assertRaises(TypeError):
            mark = User('Mark', 'Watney', password='valid')  # noqa

    def test_credentials_init_positional(self):
        with self.assertRaises(TypeError):
            mark = User('Mark', 'Watney', 'mwatney', 'valid')  # noqa

    def test_credentials_init_keyword(self):
        mark = User('Mark', 'Watney', username='mwatney', password='valid')
        self.assertEqual(mark.username, 'mwatney')
        self.assertEqual(mark.password, ENCRYPTED_PASSWORD)

    def test_password_repr(self):
        mark = User('Mark', 'Watney', username='mwatney', password='valid')
        result = "User('Mark', 'Watney', password='*****')"
        self.assertEqual(repr(mark), result)
