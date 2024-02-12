
class Iris:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str

    def __init__(self, sl, sw, pl, pw, species) -> None:
        self.sepal_length = sl
        self.sepal_width = sw
        self.petal_length = pl
        self.petal_width = pw
        self.species = species

    @property
    def numeric_values(self):
        return [x for x in vars(self).values() if type(x) is float]

    def sum(self) -> float:
        return sum(self.numeric_values)

    def len(self) -> int:
        return len(self.numeric_values)

    def mean(self) -> float:
        return self.sum() / self.len()
