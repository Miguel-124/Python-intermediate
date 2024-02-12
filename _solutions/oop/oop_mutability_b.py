
@dataclass
class User:
    firstname: str
    lastname: str
    groups: list[str] = field(default_factory=list)
