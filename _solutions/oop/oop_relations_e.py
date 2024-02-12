
@dataclass
class Address:
    street: str
    city: str
    postcode: int
    region: str
    country: str


@dataclass
class User:
    firstname: str
    lastname: str
    addresses: list[Address | None]


def convert(contact: dict) -> User:
    addresses = map(lambda x: Address(**x), contact.pop('addresses'))
    return User(**contact, addresses=list(addresses))

result = map(convert, DATA)
