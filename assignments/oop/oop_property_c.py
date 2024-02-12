"""
* Assignment: OOP Property NumericValues
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Modify class `Iris`
    2. Create property `numeric_values`,
       which returns a tuple of values of all `float` type attributes
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `Iris`
    2. Stwórz property `numeric_values`,
       który zwraca typlę wartości wszystkich atrybutów typu `float`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `var(self)`
    * `dict.values()`
    * `instanceof()`
    * `type()`
    * `@property`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert hasattr(Iris, '__init__')
    >>> assert hasattr(Iris, 'numeric_values')
    >>> assert not isfunction(Iris.numeric_values)

    >>> assert Iris.numeric_values.__class__ is property
    >>> assert Iris.numeric_values.fdel is None
    >>> assert Iris.numeric_values.fset is None
    >>> assert Iris.numeric_values.fget is not None

    >>> setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
    >>> setosa.numeric_values
    (5.1, 3.5, 1.4, 0.2)
"""


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

    # Create property `numeric_values`,
    # which returns a tuple of values of all `float` type attributes
    # type: Callable[[], tuple[float]]
    @property
    def numeric_values(self):
        return tuple(x for x in vars(self).values() if type(x) is float)


