
class User:
    def __init__(self, firstname, lastname, email, phone, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self._email = email
        self._phone = phone
        self.__username = username
        self.__password = password
