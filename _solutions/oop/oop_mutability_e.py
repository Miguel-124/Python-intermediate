
@dataclass
class Hero:
    name: str
    health: int = field(default_factory=lambda: randint(50, 100))
