
@dataclass
class Point:
    x: int = 0
    y: int = 0


@dataclass
class Path:
    points: list[Point] = field(default_factory=list)
