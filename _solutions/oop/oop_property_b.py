
@dataclass
class User:
    firstname: str
    lastname: str
    birthdate: date

    @property
    def age(self):
        today = date.today()
        days = (today - self.birthdate).days
        return int(days / YEAR)
