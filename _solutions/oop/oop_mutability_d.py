
class Hero:
    name: str
    health: int

    def __init__(self, name):
        self.name = name
        self.health = randint(50, 100)
