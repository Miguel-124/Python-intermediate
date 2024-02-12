
@dataclass
class Point:
    x: int
    y: int
    z: int

    @property
    def position(self):
        return self.x, self.y, self.z
